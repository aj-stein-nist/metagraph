DEFAULT_XMLNS = 'http://csrc.nist.gov/ns/oscal/metaschema/1.0'

class MetaschemaElement:
    def __init__(self, tag=None, attrs=None, xmlns=None):
        self.tag = tag
        self.qname = f"{{{xmlns}}}{tag}" if xmlns else f"{{{DEFAULT_XMLNS}}}{tag}"
        self.attrs = []
        self.value = ''
        self.parent = None
        self.children = []
        for k,v in dict(attrs).items():
            # With a XML parsing engine that supports namespaces but not namespace
            # prefixes by default, like Python's xml.sax, processing elements
            # in NS mode returns the key, the tag name, as a tuple, not just a
            # string when not using namespaces.
            key = k[1] if isinstance(k, tuple) else k
            normalized_key = key.replace('-', '_')
            self.attrs.append(key)
            setattr(self, normalized_key, v)
        self.xmlns = xmlns if xmlns else DEFAULT_XMLNS

class MetaschemaRoot(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MetaschemaRootName(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class Assembly(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class AssemblyReference(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class AssemblyExample(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class AssemblyGroupAs(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class AssemblyUseName(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class Constraint(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class ConstraintAllowedValues(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class ConstraintAllowedValuesEnum(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class ConstraintExpect(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class ConstraintExpectMessage(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class ConstraintHasCardinality(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class ConstraintIndex(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class ConstraintIndexHasKey(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class ConstraintIsUnique(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class ConstraintIsUniqueKeyField(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class ConstraintMatches(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class Description(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class FormalName(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class Flag(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class FlagReference(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class Field(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class FieldReference(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class FieldJsonValueKey(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class Import(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class JsonBaseUri(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class Model(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class ModelChoice(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class Namespace(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class Remarks(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class SchemaName(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class SchemaVersion(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class ShortName(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class Prop(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupElement(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupAnchor(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupBold(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupParagraph(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupHeader1(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupHeader2(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupHeader3(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupHeader4(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupHeader5(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupHeader6(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupEmphasis(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupItalics(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupStrong(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupBold(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupInline(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupQuoted(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupSubscript(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupSuperscript(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupImage(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupLink(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupCode(MetaschemaElement):
    def __init__(self, tag=None, attrs=None, xmlns=None):
        super().__init__(tag, attrs, xmlns)

class MarkupUnorderedList(MetaschemaElement):
    pass

class MarkupOrderedList(MetaschemaElement):
    pass

class MarkupListItem(MetaschemaElement):
    pass
