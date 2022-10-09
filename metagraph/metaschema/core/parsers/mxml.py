import logging
from os import environ
from xml.sax import parse
from xml.sax import make_parser
from xml.sax.handler import ContentHandler, feature_namespaces
from datatypes import *
from elements import *

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(getattr(logging, str(environ.get('METAGRAPH_LOGLEVEL', 'DEBUG')).upper()))

class MetaschemaXmlHandler(ContentHandler):
    def __init__(self):
        super().__init__()
        self.elements = []

    @property
    def current(self):
        logger.debug(f"returning last current elem, {len(self.elements) - 1}")
        return self.elements[-1]

    def startElement(self, name, attrs):
        logger.debug(f"<{name}> START")
        element = self.process(name, attrs, None)
        if element:
            logger.debug(f"element: {element}")
            logger.debug(f"element attributes: {element.attrs}")
            self.elements.append(element)
        else:
            logger.warning(f"unregistered Metaschema element {name} found")

    def startElementNS(self, name, qname, attrs):
        xmlns, ncname = name
        logger.debug(f"<{ncname} xmlns=\"{xmlns}\"> START")
        element = self.process(ncname, attrs, xmlns)
        if element:
            logger.debug(f"element: {element}")
            logger.debug(f"element attributes: {element.attrs}")
            self.elements.append(element)
        else:
            logger.warning(f"unregistered Metaschema element {ncname} found")

    def endElement(self, name):
        clean(self.current)
        if len(self.elements) > 1:
            child = self.elements.pop()
            self.current.children.append(child)
        logger.debug(f"<{name}> children: {[child.tag for child in self.current.children if child.tag]}")
        logger.debug(f"<{name}> END")

    def endElementNS(self, name, qname):
        xmlns, ncname = name
        clean(self.current)
        if len(self.elements) > 1:
            child = self.elements.pop()
            self.current.children.append(child)
            self.current.children[-1].parent = self.current
        logger.debug(f"<{ncname}> children: {[child.tag for child in self.current.children if child.tag]}")
        logger.debug(f"<{ncname} xmlns=\"{xmlns}\"> END")

    def characters(self, content):
        self.current.value += content

    def process(self, name, attrs, xmlns):
        """Process a potential Metaschema XML element and its attributes to map
        into a proper element class instance."""
        if name == 'METASCHEMA':
            return MetaschemaRoot(name, attrs, xmlns)
        if name =='assembly':
            return AssemblyReference(name, attrs, xmlns)
        if name == 'constraint':
            return Constraint(name, attrs, xmlns)
        if name == 'allowed-values':
            return ConstraintAllowedValues(name, attrs, xmlns)
        if name == 'enum':
            return ConstraintAllowedValuesEnum(name, attrs, xmlns)
        if name == 'has-cardinality':
            return ConstraintHasCardinality(name, attrs, xmlns)
        if name == 'index':
            return ConstraintIndex(name, attrs, xmlns)
        if name == 'index-has-key':
            return ConstraintIndexHasKey(name, attrs, xmlns)
        if name == 'is-unique':
            return ConstraintIsUnique(name, attrs, xmlns)
        if name == 'key-field':
            return ConstraintIsUniqueKeyField(name, attrs, xmlns)
        if name == 'matches':
            return ConstraintMatches(name, attrs, xmlns)
        if name == 'expect':
            return ConstraintExpect(name, attrs, xmlns)
        if name == 'message':
            return ConstraintExpectMessage(name, attrs, xmlns)
        if name == 'description':
            return Description(name, attrs, xmlns)
        if name == 'formal-name':
            return FormalName(name, attrs, xmlns)
        if name == 'prop':
            return Prop(name, attrs, xmlns)
        if name == 'import':
            return Import(name, attrs, xmlns)
        if name == 'json-base-uri':
            return JsonBaseUri(name, attrs, xmlns)
        if name == 'model':
            return Model(name, attrs, xmlns)
        if name == 'choice':
            return ModelChoice(name, attrs, xmlns)
        if name == 'namespace':
            return Namespace(name, attrs, xmlns)
        if name == 'remarks':
            return Remarks(name, attrs, xmlns)
        if name == 'schema-name':
            return SchemaName(name, attrs, xmlns)
        if name == 'schema-version':
            return SchemaVersion(name, attrs, xmlns)
        if name == 'short-name':
            return ShortName(name, attrs, xmlns)
        if name == 'example':
            return AssemblyExample(name, attrs, xmlns)
        if name == 'field':
            return FieldReference(name, attrs, xmlns)
        if name == 'flag':
            return FlagReference(name, attrs, xmlns)
        if name == 'define-assembly':
            return Assembly(name, attrs, xmlns)
        if name == 'define-field':
            return Field(name, attrs, xmlns)
        if name == 'define-flag':
            return Flag(name, attrs, xmlns)
        if name == 'group-as':
            return AssemblyGroupAs(name, attrs, xmlns)
        if name == 'json-value-key':
            return FieldJsonValueKey(name, attrs, xmlns)
        if name == 'use-name':
            return AssemblyUseName(name, attrs, xmlns)
        if name == 'p':
            return MarkupParagraph(name, attrs, xmlns)
        if name == 'a':
            return MarkupAnchor(name, attrs, xmlns)
        if name == 'ul':
            return MarkupUnorderedList
        if name == 'ol':
            return MarkupOrderedList(name, attrs, xmlns)
        if name == 'li':
            return MarkupListItem(name, attrs, xmlns)
        if name == 'b':
            return MarkupBold(name, attrs, xmlns)
        if name == 'em':
            return MarkupEmphasis(name, attrs, xmlns)
        if name == 'i':
            return MarkupItalics(name, attrs, xmlns)
        if name == 'img':
            return MarkupImage(name, attrs, xmlns)
        if name == 'link':
            return MarkupLink(name, attrs, xmlns)
        if name == 'code':
            return MarkupCode(name, attrs, xmlns)
        if name == 'strong':
            return MarkupStrong(name, attrs, xmlns)
        if name == 'h1':
            return MarkupHeader1(name, attrs, xmlns)
        if name == 'h2':
            return MarkupHeader2(name, attrs, xmlns)
        if name == 'h3':
            return MarkupHeader3(name, attrs, xmlns)
        if name == 'h4':
            return MarkupHeader4(name, attrs, xmlns)
        if name == 'h5':
            return MarkupHeader5(name, attrs, xmlns)
        if name == 'h6':
            return MarkupHeader6(name, attrs, xmlns)
        if name == 'inline':
            return MarkupInline(name, attrs, xmlns)
        if name == 'q':
            return MarkupQuoted(name, attrs, xmlns)
        if name == 'sub':
            return MarkupSubscript(name, attrs, xmlns)
        if name == 'sup':
            return MarkupSuperscript(name, attrs, xmlns)
        if name == 'root-name':
            return MetaschemaRootName(name, attrs, xmlns)

        return None

def clean(element):
    logger.debug(f"cleaning and deleting {element}")
    del element

if __name__ == '__main__':
    logger.debug('test Metaschema model parse start')
    handler = MetaschemaXmlHandler()
    parser = make_parser()
    parser.setFeature(feature_namespaces, True)
    parser.setContentHandler(handler)
    parser.parse('vendor/oscal/src/metaschema/oscal_ssp_metaschema.xml')
    definition = handler.current
    logger.debug('test Metaschema model parse start')
