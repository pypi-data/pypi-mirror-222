"""
a2dl | (A)sciidoc(2D)rawio(L)ibrary | https://tigabeatz.net | MIT Licence
This package generates draw.io libraries from AsciiDoc-based descriptions
and updates icons within draw.io diagrams based on those libraries.
"""

import importlib.resources
import base64
import glob
import hashlib
import json
import logging
import re
import struct
import sys
import uuid
import xml.etree.ElementTree as ET
import zlib
from os import getcwd, makedirs
from os.path import abspath, join, dirname, basename
from shutil import copytree
from urllib.parse import unquote


def get_package_data_path(filename:str, p:bool = False) -> str:
    if p:
        ref = importlib.resources.files('a2dl.data') / filename
        with importlib.resources.as_file(ref) as path:
            strpath = str(path)
        return strpath
    else:
        return f'data/{filename}'


# The following string determines the file search pattern:
GLOB_STRING = '**/*.adoc'  # Search for all adoc files recursively

# Detecting relevant lines in files can be customized with the following strings:
ADOC_VARIABLE_IDENTIFIER = [["==", "===", "====", "====="],
                            ":variable_name:"]  # Extract content afer each identifier until the next occurrence of i in [0]
ADOC_ICON_IDENTIFIER = ":icon_image_rel_path:"
ADOC_ICON_TITLE_IDENTIFIER = ":icon_name:"
ADOC_ICON_MORE_IDENTIFIER = ":read_more:"
LINES2SKIP = ['[quote', 'image::']  # skips lines starting with

# Formatting of the Tooltip can be customized with the following strings:
HTML_TOOLTIP = '<h1 class="dio_tooltip" >%name%</h1>'  # The HTML for each section will get appended to this string
HTML_SECTION = '<h2 class="dio_tooltip" >{}</h2>%{}%'  # variable['title'], variable['name']
HTML_WARNING = '<b class="dio_tooltip" >{}</b>'

# "read more" will be the last line in the html tooltip
HTML_MORE_BASEURL = '{}'  # 'or: use a base ur like https://example.com/{}
#      if articles details page share the same base url'
HTML_MORE = '<br> <a href="{}" target="_more">Image generated with Stable Diffusion</a>'

# Icon styling
ICON_STYLE = "rounded=1;whiteSpace=wrap;html=1;"

# If sections include images as .png, these will be encoded and included. The image styling can be modified:
IMAGE_STYLE = 'fillColor=none;rounded=1;shape=image;verticalLabelPosition=bottom;labelBackgroundColor=default;verticalAlign=top;aspect=fixed;imageAspect=0;image=data:image/{},{};'  # The type and image data are set from the file

# Generator settings
ARTICLE_TEMPLATE = 'data/template_article.adoc'
IMAGES_PATH = 'data/images'
IMAGES_GLOB_STRING = '**/*.png'
IMAGES_WIDTH = "70"
IMAGES_HEIGHT = "70"

# create logger
logger = logging.getLogger('a2dl')
logger.setLevel(logging.INFO)
sh = logging.NullHandler()
sh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
sh.setFormatter(formatter)
logger.addHandler(sh)


class Diagicon:
    """
    A class to represent a Draw.IO Icon, allowing conversion from AsciiDoc files to Draw.IO diagram files.

    Example Usage:

    >>> my_icon = Diagicon()
    >>> x = my_icon.from_adoc(get_package_data_path('exampleDocument.adoc'))
    >>> # write the icon to a Diagram file
    >>> my_icon.write_diagram(get_package_data_path('test-generated-icon-from-exampleDocument.drawio'))

    """

    def __init__(self, iconid: str = None, name: str = None):
        """ Initializes a new diagicon instance.

        :param iconid: The unique ID for the icon. If none is provided, a UUID is generated.
        :param name:  The name for the icon. If none is provided, the id is used.
        """
        self.tooltip = HTML_TOOLTIP
        self.html_section = HTML_SECTION

        if not iconid:
            self.iconid = str(uuid.uuid1())
        else:
            self.iconid = iconid
        if not name:
            self.name = self.iconid
        else:
            self.name = name

        self.placeholders: str = "1"
        self.link: str = None
        self.image: str = None
        self.variables: list = None  # [{"title":label, "name":label, "content":[] }]
        self.parent: str = "1"
        self.vertex: str = "1"
        self.x: str = "80"  # NEED 4 DIAGRAM
        self.y: str = "160"  # NEED 4 DIAGRAM
        self.width: str = "160"  # NO FUNCTION
        self.height: str = "160"  # NO FUNCTION
        self.style = ICON_STYLE
        self.image_base_path: str = None

    @staticmethod
    def __read_diagram2dict__(filename: str) -> list:
        """
        read a draw.io diagram and return as dict

        >>> retval = Diagicon.__read_diagram2dict__(get_package_data_path('exampleDiagram.drawio'))
        >>> hashlib.sha256(json.dumps(retval, sort_keys=True).encode('utf-8')).hexdigest()
        '3689e6d92d8cce691334888734486e683c865af6f6e5ff1111474aca920c7e0f'
        """

        tree = ET.parse(filename)
        root = tree.getroot()

        # data = base64.b64decode(root.text)
        # xml = zlib.decompress(data, wbits=-15)
        # xml = unquote(xml.decode('utf-8'))

        xmlobjects = []

        for xmldict in root:
            for xmlobject in xmldict[0][0]:
                if xmlobject.tag == 'object':
                    icon = {"tag": xmlobject.tag, "attrib": xmlobject.attrib, "elements": []}
                    for el in xmlobject:
                        icon['elements'].append({"tag": el.tag, "attrib": el.attrib, "elements": []})
                        for shape in el:
                            icon['elements'].append({"tag": shape.tag, "attrib": shape.attrib})
                    xmlobjects.append(icon)

        return xmlobjects

    @staticmethod
    def __get_base64_encoded_image__(image_path: str):
        try:
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode('utf-8')
        except FileNotFoundError as err:
            logger.error(err)

    @staticmethod
    def __get_image_size__(file_path: str):
        try:
            with open(file_path, 'rb') as f:
                data = f.read(24)
            if len(data) != 24:
                logger.warning(f'The file {file_path} is not a PNG image.')
                return None, None
            if data[:8] != b'\x89PNG\r\n\x1a\n':
                logger.warning(f'The file {file_path} is not a PNG image.')
                return None, None

            width, height = struct.unpack('>LL', data[16:24])
            logger.debug(f'The file {file_path} is a PNG image with width: {width} and height: {height}.')

            return width, height
        except FileNotFoundError as err:
            logging.error(str(err))

    def __as_object__(self, parent: ET.Element = None) -> ET.Element:
        if parent:
            xmlobject = ET.SubElement(parent, "object")
        else:
            xmlobject = ET.Element("object")

        xmlobject.set("id", self.iconid)
        xmlobject.set("label", self.name)  # SPECIAL used when icon is used library
        xmlobject.set("name", self.name)
        xmlobject.set("placeholders", self.placeholders)
        xmlobject.set("tooltip", self.tooltip)

        # any custom fields
        for variable in self.variables:
            vt = ''
            for l in variable['content']:
                vt = vt + str(l)
            xmlobject.set(variable['name'], vt)
            self.tooltip = self.tooltip + self.html_section.format(variable['title'], variable['name'])

        # add readmore
        if self.link:
            xmlobject.set("link", HTML_MORE_BASEURL.format(self.link))
            self.tooltip = self.tooltip + HTML_MORE.format(HTML_MORE_BASEURL.format(self.link))

        mxCell = ET.SubElement(xmlobject, "mxCell")
        mxCell.set("parent", self.parent)
        mxCell.set("vertex", self.vertex)

        # image
        if self.image:
            if self.image.endswith('.png'):
                self.width, self.height = self.__get_image_size__(self.image)
                if self.width:
                    mxCell.set("style", IMAGE_STYLE.format('png', self.__get_base64_encoded_image__(self.image)))
            else:
                logger.warning('fileformat for {} not implemented: {}'.format(self.name, self.image))

        mxGeometry = ET.SubElement(mxCell, "mxGeometry")
        mxGeometry.set("x", str(self.x))
        mxGeometry.set("y", str(self.y))
        mxGeometry.set("width", str(self.width))
        mxGeometry.set("height", str(self.height))
        mxGeometry.set("as", "geometry")

        return xmlobject

    def __as_diagram__(self) -> ET.Element:
        # The element tree
        mxfile = ET.Element("mxfile")
        diagram = ET.SubElement(mxfile, "diagram",
                                name="Page-1", id=str(uuid.uuid1()))
        mxGraphModel = ET.SubElement(diagram, "mxGraphModel",
                                     dx="1114", dy="822", grid="1", gridSize="10",
                                     guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1",
                                     pageScale="1", pageWidth="1169", pageHeight="827", math="0", shadow="0")
        root = ET.SubElement(mxGraphModel, "root")
        mxCelldiag1 = ET.SubElement(root, "mxCell",
                                    id="0")
        mxCelldiag2 = ET.SubElement(root, "mxCell",
                                    id="1", parent="0")
        xmlobject = self.__as_object__(root)
        return mxfile

    def as_object(self, parent: ET.Element = None) -> ET.Element:
        """to embed in other xml structures"""
        return self.__as_object__(parent)

    def as_object_s(self) -> str:
        """to embed in other library xml structures"""
        mxGraphModel = ET.Element("mxGraphModel")
        root = ET.SubElement(mxGraphModel, "root")
        mxCelldiag1 = ET.SubElement(root, "mxCell",
                                    id="0")
        mxCelldiag2 = ET.SubElement(root, "mxCell",
                                    id="1", parent="0")
        asd = self.__as_object__(parent=root)
        rt = None
        try:
            rt = ET.tostring(mxGraphModel).decode(encoding='utf-8')
        except Exception as err:
            logger.error(f'{self.name} {self.iconid} {err}')
        return rt

    def as_diagram_s(self) -> str:
        """return a string of diagram xlm"""
        xmlstr = ET.tostring(self.__as_diagram__())
        return xmlstr

    def write_diagram(self, file: str):
        """write as a diagram file"""
        tree = ET.ElementTree(self.__as_diagram__())
        tree.write(abspath(file))

    @staticmethod
    def linerules(oline: str) -> str:
        """add special line handling, like make asciidoc url to html url"""
        # exchange link
        if "http" in oline:
            # get url, domain, link description "(^http.?://(.*))\[(.*)\]"
            words = oline.split()
            uline = oline
            for word in words:
                m = re.search("(^http.?://(.*))\[(.*)\]", word)
                # todo: change regex, such that any text inside the [] works (breaks with whitespace, actually)
                if m:
                    # logger.debug(m.group(3))
                    if len(m.group(3)) < 3:
                        mn = '<a href="{}" target="_blank">{}<a>'.format(m.group(1), m.group(2))
                    else:
                        mn = '<a href="{}" target="_blank">{}<a>'.format(m.group(1), m.group(3))
                    uline = oline.replace(m.group(0), mn)
                    # logger.debug(uline)
            logger.debug(f'replacing {oline} with {uline}')
            return uline

        # replace Warning
        elif oline.startswith('WARNING:'):
            uline = HTML_WARNING.format(oline.strip("WARNING:").strip())
            logger.debug(f'replacing {oline} with {uline}')
            return uline

        else:

            # strip adoc image lines, quotes and such
            for stripsign in LINES2SKIP:
                if oline.startswith(stripsign):
                    uline = ''
                    logger.debug(f'replacing {oline} with {uline}')
                    return uline

            return oline

    def from_adoc(self, filename: str, parent: ET.Element = None):
        """set from adoc and return as object"""

        def get_data(lines):
            variables = []
            icon_full_path = None
            starts = []

            def extract(s, e):
                c = []
                i = 0
                for eline in lines:
                    if s + 3 <= i <= e:
                        # c.append(line)
                        found = False
                        for l2_ident in ADOC_VARIABLE_IDENTIFIER[0]:
                            if eline.startswith(l2_ident):
                                found = True
                        if not found:
                            # special line handling, like make url tags ...
                            nline = self.linerules(eline)
                            c.append(nline)
                        else:
                            break
                    i += 1
                return c

            # start
            line_number = 0
            for line in lines:
                # --> the variables are repeated
                for l1_ident in ADOC_VARIABLE_IDENTIFIER[0]:
                    if line.startswith(l1_ident) and lines[line_number + 1].startswith(ADOC_VARIABLE_IDENTIFIER[1]):
                        variables.append({
                            "title": line.strip(l1_ident).strip(),
                            "name": lines[line_number + 1].strip(ADOC_VARIABLE_IDENTIFIER[1]).strip(),
                            "start": line_number,
                        })
                        starts.append(line_number)
                        break

                if line.startswith(ADOC_ICON_IDENTIFIER):
                    if not self.image_base_path:
                        icon_full_path = abspath(join(dirname(filename), line.strip(ADOC_ICON_IDENTIFIER).strip()))
                    else:
                        icon_full_path = abspath(join(self.image_base_path, line.strip(ADOC_ICON_IDENTIFIER).strip()))
                    self.icon = icon_full_path

                if line.startswith(ADOC_ICON_TITLE_IDENTIFIER):
                    self.name = line.strip(ADOC_ICON_TITLE_IDENTIFIER).strip()

                if line.startswith(ADOC_ICON_MORE_IDENTIFIER):
                    self.link = line.strip(ADOC_ICON_MORE_IDENTIFIER).strip()

                line_number += 1

            # end
            for variable in variables:
                cnt = 0
                for start in starts:
                    if variable['start'] == start:
                        try:
                            variable['end'] = starts[cnt + 1] - 1
                        except Exception as err:
                            variable['end'] = len(lines)
                            logging.debug(err)
                    cnt += 1

            # content
            for variable in variables:
                variable['content'] = extract(variable['start'], variable['end'])

            return variables, icon_full_path

        try:
            with open(filename, "r") as file:
                fileslines = file.readlines()

            self.variables, self.image = get_data(fileslines)
            logger.debug(f'{filename} {len(self.variables)} {self.image}')

            if len(self.variables) == 0 and not self.image:
                raise ValueError('is not an icon file and will be sKipped')
            else:
                return self.__as_object__(parent)

        except FileNotFoundError as err:
            logger.error(err)

        return None


class Diaglibrary:
    """
    A class to represent a Draw.IO Library which handles collections of `Diagicon` objects.

    Example Usage:

    # by image
    >>> my_icon = Diagicon(name='tigabeatz')
    >>> x = my_icon.from_adoc(get_package_data_path('exampleDocument.adoc'))
    >>> my_library = Diaglibrary()
    >>> my_library.icons.append(my_icon)
    >>> my_library.write(get_package_data_path('test-generated-library-from-exampleDocument.xml'))

    # from folder
    >>> my_library2 = Diaglibrary()
    >>> my_library2.from_folder(get_package_data_path('.'))
    >>> my_library2.write(get_package_data_path('test-generated-library-from-data-folder.xml'))

    """

    def __init__(self, libraryid: str = None, name: str = None):
        """ Initializes a new diaglibrary instance.

        :param libraryid:
        :param name:
        """

        if not libraryid:
            self.libraryid = str(uuid.uuid1())
        else:
            self.libraryid = libraryid

        self.name: str = name
        self.icons: list[Diagicon] = []  # instances of type icon
        self.w: int = 50
        self.h: int = 50
        self.image_base_path: str = None

    def __backup__(self):
        """ backup the library if overwrite """
        pass

    def __as_object__(self) -> ET.Element:

        mxlibrary = ET.Element("mxlibrary")
        tmpl = []
        for icn in self.icons:
            tmpl.append(
                {
                    "xml": icn.as_object_s(),
                    "w": self.w,
                    "h": self.h
                })

        mxlibrary.text = json.dumps(tmpl, indent=2)
        return mxlibrary

    @staticmethod
    def __read_library2dict__(filename: str) -> list:
        """
        read a draw.io library and return as dict

        >>> hashlib.sha256(json.dumps(Diaglibrary.__read_library2dict__(get_package_data_path('exampleLibrary.xml')), sort_keys=True).encode('utf-8')).hexdigest()
        '6b243484f07fa2e04c382b834e962c58377475f4b005f6ca2836e1bfa05b5af1'
        """

        tree = ET.parse(abspath(filename))
        root = tree.getroot()
        data = json.loads(root.text)
        xmlobjects = []

        for xmldict in data:
            xmlobject = ET.fromstring(xmldict['xml'])
            icon = {"tag": xmlobject[0].tag, "elements": []}
            for el in xmlobject[0]:
                icon['elements'].append({"tag": el.tag, "attrib": el.attrib})
            xmlobjects.append(icon)

        return xmlobjects

    def write(self, file: str):
        """write as a library file"""
        try:
            tree = ET.ElementTree(self.__as_object__())
            tree.write(abspath(file))
        except TypeError as err:
            logger.critical(f'{file} {err}')

    def from_folder(self, path: str):
        files = glob.glob(join(abspath(path), GLOB_STRING), recursive=True)
        for file in files:
            try:
                icn = Diagicon()
                icn.image_base_path = self.image_base_path
                icn.from_adoc(file)
                self.icons.append(icn)
            except ValueError as wrn:
                logger.warning(f'{file}, {wrn}')
            except Exception as err:
                logger.error(f'{file}, {err}')

        logger.info(f'files: {len(files)} ')
        logger.info(f'icons: {len(self.icons)} ')

        for logicon in self.icons:
            logger.debug(f'{logicon.variables} {logicon.image}')


class Diagdiagram:
    """
    A class to represent a Draw.IO Diagram.

    This class enables the manipulation and updating of Draw.IO Diagrams
    based on provided libraries of icons (Diaglibrary).

    Usage example:

    >>> # create library
    >>> DL = Diaglibrary()
    >>> DL.image_base_path = get_package_data_path('.')
    >>> DL.from_folder(get_package_data_path('.'))
    >>> # read Diagran
    >>> DG = Diagdiagram()
    >>> DG.from_file(get_package_data_path('exampleDiagramFromLibrary-old.drawio'))
    >>> # set options
    >>> DG.clean = False # remove backup files
    >>> DG.backup = 'test-.$exampleDiagramFromLibrary-old.drawio.bkp'
    >>> DG.new_file = True  # set False to overwrite file or True to overwrite {filename}.new.drawio. will not create a backup, if set
    >>> # update Diagram
    >>> DG.update(libraries=[DL])
    >>> # update a compressed Diagram
    >>> DG.from_file(get_package_data_path('exampleDiagramFromLibrary-compressed-old.drawio'))
    >>> DG.update(libraries=[DL])

    """

    def __init__(self):
        """ Initializes a new diagDiagram instance. """
        self.filepath: str = None  # of str
        self.objects: xml.etree.ElementTree.Element = None  # of xml.etree.ElementTree.Element
        self.stamps = []  # of __stamp__
        self.tree: xml.etree.ElementTree = None  # of xml.etree.ElementTree
        self.libraries = []  # of Diaglibrary
        self.backup = None  # set by self.from_file()
        self.clean: bool = False  # remove backup files
        self.was_compressed: bool = False  # if read a compressed file
        self.new_file: bool = True  # set False to overwrite file or True to overwrite {filename}.new.drawio

    def __backup__(self):
        """ backup the original diagram -> rename as .${filename}.bkp """
        if self.backup:
            if not self.new_file:
                os.rename(abspath(self.filepath), self.backup)

    def __restore__(self):
        """ restore the original diagram -> rename as filename """
        if self.backup and os.path.exists(self.backup):
            if not self.new_file:
                os.rename(self.backup, abspath(self.filepath))

    def __clean__(self):
        """ remove backup files"""
        if self.backup and self.clean and os.path.exists(self.backup):
            if not self.new_file:
                os.remove(self.backup)

    def __handle_compressed__(self, data):

        def pako_inflate_raw(data):
            # https://crashlaker.github.io/programming/2020/05/17/draw.io_decompress_xml_python.html
            decompress = zlib.decompressobj(-15)
            decompressed_data = decompress.decompress(data)
            decompressed_data += decompress.flush()
            return decompressed_data

        compdat = data.find('.//diagram').text

        a = base64.b64decode(compdat)
        b = pako_inflate_raw(a)
        c = unquote(b.decode())

        dat = ET.fromstring(c)

        # todo:
        #      update self.tree

        return dat

    def __stamp__(self, xmlobject: ET.Element) -> tuple[str, str, str, str]:
        """
        get an icons name, label, hash of the image, hash of the attributes
        :param xmlobject: xml.etree.ElementTree.Element
        :return: (str, str, str, str)
        """

        mxcell = xmlobject.find('mxCell')

        sattribs = str(xmlobject.items())
        sname = str(xmlobject.get('name'))
        slabel = str(xmlobject.get('label'))

        try:
            simage = str(mxcell.get('style').split('image=data:image/png,')[1].strip(';'))
        except AttributeError as err:
            logger.warning(f'{err}, {self.filepath}')
            raise ValueError('no image')

        return (sname, slabel, hashlib.sha256(simage.encode('utf-8')).hexdigest(), hashlib.sha256(
            sattribs.encode('utf-8')).hexdigest())

    def __read__(self):
        self.tree = ET.parse(abspath(self.filepath))
        root = self.tree.getroot()
        self.objects = root.findall('.//object')

        if not self.objects:
            self.objects = self.__handle_compressed__(root).findall('.//object')
            self.was_compressed = True

        # stamp each icon for a later update
        for xmlobject in self.objects:
            self.stamps.append(self.__stamp__(xmlobject))

        # if self.was_compressed:
        #     raise NotImplementedError('Working with compressed Diagrams is not properly implemented right now')

    def from_file(self, filepath: str):
        """
        Reads a diagram file and initializes the Diagdiagram object.

        >>> DG = Diagdiagram()
        >>> DG.from_file(get_package_data_path('exampleDiagramFromLibrary-old.drawio'))
        >>> basename(DG.filepath)
        'exampleDiagramFromLibrary-old.drawio'
        """
        self.filepath = filepath
        if not self.backup:
            self.backup = abspath(join(dirname(self.filepath), f'.${basename(self.filepath)}.bkp'))
        # read diagram file
        self.__read__()

    def update(self, libraries: list):
        """
        Updates the diagram based on the provided libraries.

        >>> DL = Diaglibrary()
        >>> DL.image_base_path = get_package_data_path('.')
        >>> DL.from_folder(get_package_data_path('.'))
        >>> DG = Diagdiagram()
        >>> DG.from_file(get_package_data_path('exampleDiagramFromLibrary-old.drawio'))
        >>> DG.update(libraries=[DL])
        >>> len(DG.libraries)
        1
        """

        self.libraries = libraries
        root = self.tree.getroot()

        for icnlib in self.libraries:
            # update per library and icon
            for icn in icnlib.icons:
                # update the object within the diagram
                try:

                    object_element = root.findall(f".//object[@name='{icn.name}']")
                    for diagram_icon in object_element:
                        # diagramme icon
                        diagram_cel = diagram_icon.find("mxCell")

                        # library icon
                        library_icon = icn.__as_object__()  # diagram_cel
                        library_cel = library_icon.find("mxCell")

                        # replace attributes
                        logger.info(f'working at {self.filepath}')
                        for li in library_icon.attrib:
                            if not li == 'id' and not li == 'name':
                                logger.info(f'updating {li} in icon {icn.name} ')
                                if li == 'tooltip':
                                    diagram_icon.set(li, library_icon.get(li))  # escape(library_icon.get(li))
                                else:
                                    diagram_icon.set(li, library_icon.get(li))

                        for di in library_cel.attrib:
                            if not di == 'id' and not di == 'name':
                                logger.info(f'updating {di} in icon {icn.name} ')
                                diagram_cel.set(di, library_cel.get(di))

                except AttributeError as err:
                    logger.error(f'{err} with file {self.filepath}')

        # write updated file
        self.__backup__()
        try:
            if not self.new_file:
                self.tree.write(abspath(self.filepath))
            else:
                self.tree.write(abspath(self.filepath + '.new.drawio'))
        except Exception as err:
            logger.error(f'{err} with file {self.filepath}')
            self.__restore__()

        # if enabled, remove backup files
        self.__clean__()

        logger.info(f'Updated: {self.filepath}')


def make_example(target_path: str = 'test/'):
    """  Generates a folder with articles images library

    >>> make_example()

    """

    def apply_template(image_name="", image_link="", image_alt_text="", image_h=IMAGES_HEIGHT, image_w=IMAGES_WIDTH,
                       image_rel_path=""):
        """
        :icon_image_rel_path: {{image_rel_path}}
        :icon_name: {{image_name}}
        :read_more: {{image_link}}
        [[sec-{{image_name}}]]
        == {{image_name}}
        image::{icon_image_rel_path}[{{image_alt_text}},{{image_w}},{{image_h}},float="right"]
        === {{image_name}} Summary
        """

        searchies = [
            ('{{image_name}}', image_name.strip('\n').strip())
            , ('{{image_link}}', image_link.strip('\n').strip())
            , ('{{image_alt_text}}', image_alt_text.strip('\n').strip())
            , ('{{image_h}}', image_h.strip('\n').strip())
            , ('{{image_w}}', image_w.strip('\n').strip())
            , ('{{image_rel_path}}', image_rel_path.strip('\n').strip())
        ]

        try:
            nt = []
            with open(abspath(ARTICLE_TEMPLATE), "r") as file:
                fileslines = file.readlines()
                for line in fileslines:
                    for searcher in searchies:
                        if searcher[0] in line:
                            line = line.replace(searcher[0], str(searcher[1]))
                    nt.append(line)
            return nt
        except FileNotFoundError as err:
            logger.error(err)

        return None

    # create dir
    makedirs(dirname(abspath(target_path)), exist_ok=True)

    # images
    images = glob.glob(join(abspath(IMAGES_PATH), IMAGES_GLOB_STRING), recursive=True)
    # IMAGES_PATH = get_package_data_path(abspath(target_path))
    try:
        copytree(get_package_data_path('images', p=True), abspath(target_path), dirs_exist_ok=True)
    except FileNotFoundError as err:
        logger.error(err)
        copytree(get_package_data_path('images'), abspath(target_path), dirs_exist_ok=True)

    # generate icons, articles and library
    library = Diaglibrary()
    for imagepath in images:
        icon = Diagicon()

        # article
        article = (
            apply_template(
                image_name=basename(imagepath).strip(".png"),
                image_rel_path=join(abspath(target_path), basename(imagepath)),
                image_link=f"#{basename(imagepath).strip('.png')}",
                image_alt_text=f'image {basename(imagepath)} is a random generated image',
                image_h=IMAGES_WIDTH,
                image_w=IMAGES_HEIGHT
            ),
            basename(imagepath)
        )
        tap = join(abspath(target_path), f'{basename(imagepath).strip(".png")}.adoc')

        targetarticle = open(tap, "w")
        targetarticle.writelines(article[0])
        targetarticle.close()

        # icon
        x = icon.from_adoc(tap)
        icon.image = imagepath
        icon.width = IMAGES_WIDTH
        icon.height = IMAGES_HEIGHT

        library.icons.append(icon)

    # library
    library.w = IMAGES_WIDTH
    library.h = IMAGES_HEIGHT
    library.write(join(target_path, 'test-generated-library.xml'))


def cli():
    if not len(sys.argv) == 3:
        logger.critical(
            "The script is called with {} arguments, but needs at least two: "
            "-> 'a2dl --library path/to/folder-to-scan path/to/library-file-to-write.xml' "
            "-> 'a2dl --diagram path/to/folder-to-scan path/to/file-to-update' "
            "-> 'a2dl --example path/to/folder-to-write".format(
                len(sys.argv) - 1))
        sys.exit(1)
    else:

        cwd = getcwd()
        logger.info(f'workdir: {cwd}')

        if sys.argv[1] == '--example' and sys.argv[2]:
            logger.info(f'Creating Example {sys.argv[2]}')
            make_example(sys.argv[2])
            logger.info(f'Done with creating example {sys.argv[2]}')
        elif sys.argv[1] == '--library' and sys.argv[2] and sys.argv[3]:
            logger.info('source: {} '.format(sys.argv[2]))
            logger.info('target: {} '.format(sys.argv[3]))

            logger.info('Creating library')
            my_library2 = Diaglibrary()
            my_library2.from_folder(sys.argv[2])
            my_library2.write(sys.argv[3])
            logger.info('Done with creating library')

        elif sys.argv[1] == '--diagram' and sys.argv[2] and sys.argv[3]:
            logger.info('source: {} '.format(sys.argv[2]))
            logger.info('target: {} '.format(sys.argv[3]))

            DL = Diaglibrary()
            DL.from_folder(sys.argv[2])

            logger.info('Updating Diagram')
            DG = Diagdiagram()
            DG.from_file(sys.argv[3])
            DG.update(libraries=[DL])
            logger.info('Done with updating Diagram')


if __name__ == '__main__':
    # todo: - func: icons without images
    #       -- handle in diagram update function when there is no PNG
    #       - func: apply a style template on icons and exports
    #       -- default box / style for non image/image error
    #       - func: example project: use folders :-)
    #       - code: use argparse, importlib.resources
    #       -- critical: adoc files need empty line as last line, assure that before going to convert to html

    cli()
