// Copyright 2009 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package dwarf provides access to DWARF debugging information loaded from
// executable files, as defined in the DWARF 2.0 Standard at
// http://dwarfstd.org/doc/dwarf-2.0.0.pdf
package dwarf

import (
	"encoding/binary"
	"errors"
)

// Data represents the DWARF debugging information
// loaded from an executable file (for example, an ELF or Mach-O executable).
type Data struct {
	// raw data
	abbrev   []byte
	aranges  []byte
	frame    []byte
	info     []byte
	line     []byte
	pubnames []byte
	ranges   []byte
	str      []byte

	// New sections added in DWARF 5.
	addr       []byte
	lineStr    []byte
	strOffsets []byte

	// parsed data
	abbrevCache map[uint64]abbrevTable
	bigEndian   bool
	order       binary.ByteOrder
	typeCache   map[Offset]Type
	typeSigs    map[uint64]*typeUnit
	unit        []unit
}

// New returns a new Data object initialized from the given parameters.
// Rather than calling this function directly, clients should typically use
// the DWARF method of the File type of the appropriate package debug/elf,
// debug/macho, or debug/pe.
//
// The []byte arguments are the data from the corresponding debug section
// in the object file; for example, for an ELF object, abbrev is the contents of
// the ".debug_abbrev" section.
func New(abbrev, aranges, frame, info, line, pubnames, ranges, str []byte) (*Data, error) {}

// AddTypes will add one .debug_types section to the DWARF data. A
// typical object with DWARF version 4 debug info will have multiple
// .debug_types sections. The name is used for error reporting only,
// and serves to distinguish one .debug_types section from another.
func (d *Data) AddTypes(name string, types []byte) error {}

// AddSection adds another DWARF section by name. The name should be a
// DWARF section name such as ".debug_addr", ".debug_str_offsets", and
// so forth. This approach is used for new DWARF sections added in
// DWARF 5 and later.
func (d *Data) AddSection(name string, contents []byte) error {}

func (i Attr) String() string {}

type DecodeError struct {
	Name   string
	Offset Offset
	Err    string
}

func (e DecodeError) Error() string {}

func (i Class) String() string {}

//go:generate stringer -type Attr -trimprefix=Attr

// An Attr identifies the attribute type in a DWARF Entry's Field.
type Attr uint32

const (
	AttrSibling        Attr = 0x01
	AttrLocation       Attr = 0x02
	AttrName           Attr = 0x03
	AttrOrdering       Attr = 0x09
	AttrByteSize       Attr = 0x0B
	AttrBitOffset      Attr = 0x0C
	AttrBitSize        Attr = 0x0D
	AttrStmtList       Attr = 0x10
	AttrLowpc          Attr = 0x11
	AttrHighpc         Attr = 0x12
	AttrLanguage       Attr = 0x13
	AttrDiscr          Attr = 0x15
	AttrDiscrValue     Attr = 0x16
	AttrVisibility     Attr = 0x17
	AttrImport         Attr = 0x18
	AttrStringLength   Attr = 0x19
	AttrCommonRef      Attr = 0x1A
	AttrCompDir        Attr = 0x1B
	AttrConstValue     Attr = 0x1C
	AttrContainingType Attr = 0x1D
	AttrDefaultValue   Attr = 0x1E
	AttrInline         Attr = 0x20
	AttrIsOptional     Attr = 0x21
	AttrLowerBound     Attr = 0x22
	AttrProducer       Attr = 0x25
	AttrPrototyped     Attr = 0x27
	AttrReturnAddr     Attr = 0x2A
	AttrStartScope     Attr = 0x2C
	AttrStrideSize     Attr = 0x2E
	AttrUpperBound     Attr = 0x2F
	AttrAbstractOrigin Attr = 0x31
	AttrAccessibility  Attr = 0x32
	AttrAddrClass      Attr = 0x33
	AttrArtificial     Attr = 0x34
	AttrBaseTypes      Attr = 0x35
	AttrCalling        Attr = 0x36
	AttrCount          Attr = 0x37
	AttrDataMemberLoc  Attr = 0x38
	AttrDeclColumn     Attr = 0x39
	AttrDeclFile       Attr = 0x3A
	AttrDeclLine       Attr = 0x3B
	AttrDeclaration    Attr = 0x3C
	AttrDiscrList      Attr = 0x3D
	AttrEncoding       Attr = 0x3E
	AttrExternal       Attr = 0x3F
	AttrFrameBase      Attr = 0x40
	AttrFriend         Attr = 0x41
	AttrIdentifierCase Attr = 0x42
	AttrMacroInfo      Attr = 0x43
	AttrNamelistItem   Attr = 0x44
	AttrPriority       Attr = 0x45
	AttrSegment        Attr = 0x46
	AttrSpecification  Attr = 0x47
	AttrStaticLink     Attr = 0x48
	AttrType           Attr = 0x49
	AttrUseLocation    Attr = 0x4A
	AttrVarParam       Attr = 0x4B
	AttrVirtuality     Attr = 0x4C
	AttrVtableElemLoc  Attr = 0x4D
	// The following are new in DWARF 3.
	AttrAllocated     Attr = 0x4E
	AttrAssociated    Attr = 0x4F
	AttrDataLocation  Attr = 0x50
	AttrStride        Attr = 0x51
	AttrEntrypc       Attr = 0x52
	AttrUseUTF8       Attr = 0x53
	AttrExtension     Attr = 0x54
	AttrRanges        Attr = 0x55
	AttrTrampoline    Attr = 0x56
	AttrCallColumn    Attr = 0x57
	AttrCallFile      Attr = 0x58
	AttrCallLine      Attr = 0x59
	AttrDescription   Attr = 0x5A
	AttrBinaryScale   Attr = 0x5B
	AttrDecimalScale  Attr = 0x5C
	AttrSmall         Attr = 0x5D
	AttrDecimalSign   Attr = 0x5E
	AttrDigitCount    Attr = 0x5F
	AttrPictureString Attr = 0x60
	AttrMutable       Attr = 0x61
	AttrThreadsScaled Attr = 0x62
	AttrExplicit      Attr = 0x63
	AttrObjectPointer Attr = 0x64
	AttrEndianity     Attr = 0x65
	AttrElemental     Attr = 0x66
	AttrPure          Attr = 0x67
	AttrRecursive     Attr = 0x68
	// The following are new in DWARF 4.
	AttrSignature      Attr = 0x69
	AttrMainSubprogram Attr = 0x6A
	AttrDataBitOffset  Attr = 0x6B
	AttrConstExpr      Attr = 0x6C
	AttrEnumClass      Attr = 0x6D
	AttrLinkageName    Attr = 0x6E
	// The following are new in DWARF 5.
	AttrStringLengthBitSize  Attr = 0x6F
	AttrStringLengthByteSize Attr = 0x70
	AttrRank                 Attr = 0x71
	AttrStrOffsetsBase       Attr = 0x72
	AttrAddrBase             Attr = 0x73
	AttrRnglistsBase         Attr = 0x74
	AttrDwoName              Attr = 0x76
	AttrReference            Attr = 0x77
	AttrRvalueReference      Attr = 0x78
	AttrMacros               Attr = 0x79
	AttrCallAllCalls         Attr = 0x7A
	AttrCallAllSourceCalls   Attr = 0x7B
	AttrCallAllTailCalls     Attr = 0x7C
	AttrCallReturnPC         Attr = 0x7D
	AttrCallValue            Attr = 0x7E
	AttrCallOrigin           Attr = 0x7F
	AttrCallParameter        Attr = 0x80
	AttrCallPC               Attr = 0x81
	AttrCallTailCall         Attr = 0x82
	AttrCallTarget           Attr = 0x83
	AttrCallTargetClobbered  Attr = 0x84
	AttrCallDataLocation     Attr = 0x85
	AttrCallDataValue        Attr = 0x86
	AttrNoreturn             Attr = 0x87
	AttrAlignment            Attr = 0x88
	AttrExportSymbols        Attr = 0x89
	AttrDeleted              Attr = 0x8A
	AttrDefaulted            Attr = 0x8B
	AttrLoclistsBase         Attr = 0x8C
)

func (a Attr) GoString() string {}

// A format is a DWARF data encoding format.
type format uint32

const (
	// value formats
	formAddr        format = 0x01
	formDwarfBlock2 format = 0x03
	formDwarfBlock4 format = 0x04
	formData2       format = 0x05
	formData4       format = 0x06
	formData8       format = 0x07
	formString      format = 0x08
	formDwarfBlock  format = 0x09
	formDwarfBlock1 format = 0x0A
	formData1       format = 0x0B
	formFlag        format = 0x0C
	formSdata       format = 0x0D
	formStrp        format = 0x0E
	formUdata       format = 0x0F
	formRefAddr     format = 0x10
	formRef1        format = 0x11
	formRef2        format = 0x12
	formRef4        format = 0x13
	formRef8        format = 0x14
	formRefUdata    format = 0x15
	formIndirect    format = 0x16
	// The following are new in DWARF 4.
	formSecOffset   format = 0x17
	formExprloc     format = 0x18
	formFlagPresent format = 0x19
	formRefSig8     format = 0x20
	// The following are new in DWARF 5.
	formStrx          format = 0x1A
	formAddrx         format = 0x1B
	formRefSup4       format = 0x1C
	formStrpSup       format = 0x1D
	formData16        format = 0x1E
	formLineStrp      format = 0x1F
	formImplicitConst format = 0x21
	formLoclistx      format = 0x22
	formRnglistx      format = 0x23
	formRefSup8       format = 0x24
	formStrx1         format = 0x25
	formStrx2         format = 0x26
	formStrx3         format = 0x27
	formStrx4         format = 0x28
	formAddrx1        format = 0x29
	formAddrx2        format = 0x2A
	formAddrx3        format = 0x2B
	formAddrx4        format = 0x2C
	// Extensions for multi-file compression (.dwz)
	// http://www.dwarfstd.org/ShowIssue.php?issue=120604.1
	formGnuRefAlt  format = 0x1f20
	formGnuStrpAlt format = 0x1f21
)

//go:generate stringer -type Tag -trimprefix=Tag

// A Tag is the classification (the type) of an Entry.
type Tag uint32

const (
	TagArrayType              Tag = 0x01
	TagClassType              Tag = 0x02
	TagEntryPoint             Tag = 0x03
	TagEnumerationType        Tag = 0x04
	TagFormalParameter        Tag = 0x05
	TagImportedDeclaration    Tag = 0x08
	TagLabel                  Tag = 0x0A
	TagLexDwarfBlock          Tag = 0x0B
	TagMember                 Tag = 0x0D
	TagPointerType            Tag = 0x0F
	TagReferenceType          Tag = 0x10
	TagCompileUnit            Tag = 0x11
	TagStringType             Tag = 0x12
	TagStructType             Tag = 0x13
	TagSubroutineType         Tag = 0x15
	TagTypedef                Tag = 0x16
	TagUnionType              Tag = 0x17
	TagUnspecifiedParameters  Tag = 0x18
	TagVariant                Tag = 0x19
	TagCommonDwarfBlock       Tag = 0x1A
	TagCommonInclusion        Tag = 0x1B
	TagInheritance            Tag = 0x1C
	TagInlinedSubroutine      Tag = 0x1D
	TagModule                 Tag = 0x1E
	TagPtrToMemberType        Tag = 0x1F
	TagSetType                Tag = 0x20
	TagSubrangeType           Tag = 0x21
	TagWithStmt               Tag = 0x22
	TagAccessDeclaration      Tag = 0x23
	TagBaseType               Tag = 0x24
	TagCatchDwarfBlock        Tag = 0x25
	TagConstType              Tag = 0x26
	TagConstant               Tag = 0x27
	TagEnumerator             Tag = 0x28
	TagFileType               Tag = 0x29
	TagFriend                 Tag = 0x2A
	TagNamelist               Tag = 0x2B
	TagNamelistItem           Tag = 0x2C
	TagPackedType             Tag = 0x2D
	TagSubprogram             Tag = 0x2E
	TagTemplateTypeParameter  Tag = 0x2F
	TagTemplateValueParameter Tag = 0x30
	TagThrownType             Tag = 0x31
	TagTryDwarfBlock          Tag = 0x32
	TagVariantPart            Tag = 0x33
	TagVariable               Tag = 0x34
	TagVolatileType           Tag = 0x35
	// The following are new in DWARF 3.
	TagDwarfProcedure  Tag = 0x36
	TagRestrictType    Tag = 0x37
	TagInterfaceType   Tag = 0x38
	TagNamespace       Tag = 0x39
	TagImportedModule  Tag = 0x3A
	TagUnspecifiedType Tag = 0x3B
	TagPartialUnit     Tag = 0x3C
	TagImportedUnit    Tag = 0x3D
	TagMutableType     Tag = 0x3E // Later removed from DWARF.
	TagCondition       Tag = 0x3F
	TagSharedType      Tag = 0x40
	// The following are new in DWARF 4.
	TagTypeUnit            Tag = 0x41
	TagRvalueReferenceType Tag = 0x42
	TagTemplateAlias       Tag = 0x43
	// The following are new in DWARF 5.
	TagCoarrayType       Tag = 0x44
	TagGenericSubrange   Tag = 0x45
	TagDynamicType       Tag = 0x46
	TagAtomicType        Tag = 0x47
	TagCallSite          Tag = 0x48
	TagCallSiteParameter Tag = 0x49
	TagSkeletonUnit      Tag = 0x4A
	TagImmutableType     Tag = 0x4B
)

func (t Tag) GoString() string {}

// Location expression operators.
// The debug info encodes value locations like 8(R3)
// as a sequence of these op codes.
// This package does not implement full expressions;
// the opPlusUconst operator is expected by the type parser.
const (
	opAddr       = 0x03 /* 1 op, const addr */
	opDeref      = 0x06
	opConst1u    = 0x08 /* 1 op, 1 byte const */
	opConst1s    = 0x09 /*	" signed */
	opConst2u    = 0x0A /* 1 op, 2 byte const  */
	opConst2s    = 0x0B /*	" signed */
	opConst4u    = 0x0C /* 1 op, 4 byte const */
	opConst4s    = 0x0D /*	" signed */
	opConst8u    = 0x0E /* 1 op, 8 byte const */
	opConst8s    = 0x0F /*	" signed */
	opConstu     = 0x10 /* 1 op, LEB128 const */
	opConsts     = 0x11 /*	" signed */
	opDup        = 0x12
	opDrop       = 0x13
	opOver       = 0x14
	opPick       = 0x15 /* 1 op, 1 byte stack index */
	opSwap       = 0x16
	opRot        = 0x17
	opXderef     = 0x18
	opAbs        = 0x19
	opAnd        = 0x1A
	opDiv        = 0x1B
	opMinus      = 0x1C
	opMod        = 0x1D
	opMul        = 0x1E
	opNeg        = 0x1F
	opNot        = 0x20
	opOr         = 0x21
	opPlus       = 0x22
	opPlusUconst = 0x23 /* 1 op, ULEB128 addend */
	opShl        = 0x24
	opShr        = 0x25
	opShra       = 0x26
	opXor        = 0x27
	opSkip       = 0x2F /* 1 op, signed 2-byte constant */
	opBra        = 0x28 /* 1 op, signed 2-byte constant */
	opEq         = 0x29
	opGe         = 0x2A
	opGt         = 0x2B
	opLe         = 0x2C
	opLt         = 0x2D
	opNe         = 0x2E
	opLit0       = 0x30
	/* OpLitN = OpLit0 + N for N = 0..31 */
	opReg0 = 0x50
	/* OpRegN = OpReg0 + N for N = 0..31 */
	opBreg0 = 0x70 /* 1 op, signed LEB128 constant */
	/* OpBregN = OpBreg0 + N for N = 0..31 */
	opRegx       = 0x90 /* 1 op, ULEB128 register */
	opFbreg      = 0x91 /* 1 op, SLEB128 offset */
	opBregx      = 0x92 /* 2 op, ULEB128 reg; SLEB128 off */
	opPiece      = 0x93 /* 1 op, ULEB128 size of piece */
	opDerefSize  = 0x94 /* 1-byte size of data retrieved */
	opXderefSize = 0x95 /* 1-byte size of data retrieved */
	opNop        = 0x96
	// The following are new in DWARF 3.
	opPushObjAddr    = 0x97
	opCall2          = 0x98 /* 2-byte offset of DIE */
	opCall4          = 0x99 /* 4-byte offset of DIE */
	opCallRef        = 0x9A /* 4- or 8- byte offset of DIE */
	opFormTLSAddress = 0x9B
	opCallFrameCFA   = 0x9C
	opBitPiece       = 0x9D
	// The following are new in DWARF 4.
	opImplicitValue = 0x9E
	opStackValue    = 0x9F
	// The following a new in DWARF 5.
	opImplicitPointer = 0xA0
	opAddrx           = 0xA1
	opConstx          = 0xA2
	opEntryValue      = 0xA3
	opConstType       = 0xA4
	opRegvalType      = 0xA5
	opDerefType       = 0xA6
	opXderefType      = 0xA7
	opConvert         = 0xA8
	opReinterpret     = 0xA9
	/* 0xE0-0xFF reserved for user-specific */
)

// Basic type encodings -- the value for AttrEncoding in a TagBaseType Entry.
const (
	encAddress      = 0x01
	encBoolean      = 0x02
	encComplexFloat = 0x03
	encFloat        = 0x04
	encSigned       = 0x05
	encSignedChar   = 0x06
	encUnsigned     = 0x07
	encUnsignedChar = 0x08
	// The following are new in DWARF 3.
	encImaginaryFloat = 0x09
	encPackedDecimal  = 0x0A
	encNumericString  = 0x0B
	encEdited         = 0x0C
	encSignedFixed    = 0x0D
	encUnsignedFixed  = 0x0E
	encDecimalFloat   = 0x0F
	// The following are new in DWARF 4.
	encUTF = 0x10
	// The following are new in DWARF 5.
	encUCS   = 0x11
	encASCII = 0x12
)

// Statement program standard opcode encodings.
const (
	lnsCopy           = 1
	lnsAdvancePC      = 2
	lnsAdvanceLine    = 3
	lnsSetFile        = 4
	lnsSetColumn      = 5
	lnsNegateStmt     = 6
	lnsSetBasicBlock  = 7
	lnsConstAddPC     = 8
	lnsFixedAdvancePC = 9

	// DWARF 3
	lnsSetPrologueEnd   = 10
	lnsSetEpilogueBegin = 11
	lnsSetISA           = 12
)

// Statement program extended opcode encodings.
const (
	lneEndSequence = 1
	lneSetAddress  = 2
	lneDefineFile  = 3

	// DWARF 4
	lneSetDiscriminator = 4
)

// Line table directory directory and file name entry formats.
// These are new in DWARF 5.
const (
	lnctPath           = 0x01
	lnctDirectoryIndex = 0x02
	lnctTimestamp      = 0x03
	lnctSize           = 0x04
	lnctMD5            = 0x05
)

// Location list entry codes.
// These are new in DWARF 5.
const (
	lleEndOfList       = 0x00
	lleBaseAddressx    = 0x01
	lleStartxEndx      = 0x02
	lleStartxLength    = 0x03
	lleOffsetPair      = 0x04
	lleDefaultLocation = 0x05
	lleBaseAddress     = 0x06
	lleStartEnd        = 0x07
	lleStartLength     = 0x08
)

// Unit header unit type encodings.
// These are new in DWARF 5.
const (
	utCompile      = 0x01
	utType         = 0x02
	utPartial      = 0x03
	utSkeleton     = 0x04
	utSplitCompile = 0x05
	utSplitType    = 0x06
)

// An entry is a sequence of attribute/value pairs.
type Entry struct {
	Offset   Offset // offset of Entry in DWARF info
	Tag      Tag    // tag (kind of Entry)
	Children bool   // whether Entry is followed by children
	Field    []Field
}

// A Field is a single attribute/value pair in an Entry.
//
// A value can be one of several "attribute classes" defined by DWARF.
// The Go types corresponding to each class are:
//
//    DWARF class       Go type        Class
//    -----------       -------        -----
//    address           uint64         ClassAddress
//    block             []byte         ClassBlock
//    constant          int64          ClassConstant
//    flag              bool           ClassFlag
//    reference
//      to info         dwarf.Offset   ClassReference
//      to type unit    uint64         ClassReferenceSig
//    string            string         ClassString
//    exprloc           []byte         ClassExprLoc
//    lineptr           int64          ClassLinePtr
//    loclistptr        int64          ClassLocListPtr
//    macptr            int64          ClassMacPtr
//    rangelistptr      int64          ClassRangeListPtr
//
// For unrecognized or vendor-defined attributes, Class may be
// ClassUnknown.
type Field struct {
	Attr  Attr
	Val   interface{}
	Class Class
}

// A Class is the DWARF 4 class of an attribute value.
//
// In general, a given attribute's value may take on one of several
// possible classes defined by DWARF, each of which leads to a
// slightly different interpretation of the attribute.
//
// DWARF version 4 distinguishes attribute value classes more finely
// than previous versions of DWARF. The reader will disambiguate
// coarser classes from earlier versions of DWARF into the appropriate
// DWARF 4 class. For example, DWARF 2 uses "constant" for constants
// as well as all types of section offsets, but the reader will
// canonicalize attributes in DWARF 2 files that refer to section
// offsets to one of the Class*Ptr classes, even though these classes
// were only defined in DWARF 3.
type Class int

const (
	// ClassUnknown represents values of unknown DWARF class.
	ClassUnknown Class = iota

	// ClassAddress represents values of type uint64 that are
	// addresses on the target machine.
	ClassAddress

	// ClassBlock represents values of type []byte whose
	// interpretation depends on the attribute.
	ClassBlock

	// ClassConstant represents values of type int64 that are
	// constants. The interpretation of this constant depends on
	// the attribute.
	ClassConstant

	// ClassExprLoc represents values of type []byte that contain
	// an encoded DWARF expression or location description.
	ClassExprLoc

	// ClassFlag represents values of type bool.
	ClassFlag

	// ClassLinePtr represents values that are an int64 offset
	// into the "line" section.
	ClassLinePtr

	// ClassLocListPtr represents values that are an int64 offset
	// into the "loclist" section.
	ClassLocListPtr

	// ClassMacPtr represents values that are an int64 offset into
	// the "mac" section.
	ClassMacPtr

	// ClassMacPtr represents values that are an int64 offset into
	// the "rangelist" section.
	ClassRangeListPtr

	// ClassReference represents values that are an Offset offset
	// of an Entry in the info section (for use with Reader.Seek).
	// The DWARF specification combines ClassReference and
	// ClassReferenceSig into class "reference".
	ClassReference

	// ClassReferenceSig represents values that are a uint64 type
	// signature referencing a type Entry.
	ClassReferenceSig

	// ClassString represents values that are strings. If the
	// compilation unit specifies the AttrUseUTF8 flag (strongly
	// recommended), the string value will be encoded in UTF-8.
	// Otherwise, the encoding is unspecified.
	ClassString

	// ClassReferenceAlt represents values of type int64 that are
	// an offset into the DWARF "info" section of an alternate
	// object file.
	ClassReferenceAlt

	// ClassStringAlt represents values of type int64 that are an
	// offset into the DWARF string section of an alternate object
	// file.
	ClassStringAlt

	// ClassAddrPtr represents values that are an int64 offset
	// into the "addr" section.
	ClassAddrPtr

	// ClassLocList represents values that are an int64 offset
	// into the "loclists" section.
	ClassLocList

	// ClassRngList represents values that are an int64 offset
	// from the base of the "rnglists" section.
	ClassRngList

	// ClassRngListsPtr represents values that are an int64 offset
	// into the "rnglists" section. These are used as the base for
	// ClassRngList values.
	ClassRngListsPtr

	// ClassStrOffsetsPtr represents values that are an int64
	// offset into the "str_offsets" section.
	ClassStrOffsetsPtr
)

//go:generate stringer -type=Class

func (i Class) GoString() string {
	return "dwarf." + i.String()
}

// Val returns the value associated with attribute Attr in Entry,
// or nil if there is no such attribute.
//
// A common idiom is to merge the check for nil return with
// the check that the value has the expected dynamic type, as in:
//	v, ok := e.Val(AttrSibling).(int64)
//
func (e *Entry) Val(a Attr) interface{} {}

// AttrField returns the Field associated with attribute Attr in
// Entry, or nil if there is no such attribute.
func (e *Entry) AttrField(a Attr) *Field {}

// An Offset represents the location of an Entry within the DWARF info.
// (See Reader.Seek.)
type Offset uint32

// A Reader allows reading Entry structures from a DWARF ``info'' section.
// The Entry structures are arranged in a tree. The Reader's Next function
// return successive entries from a pre-order traversal of the tree.
// If an entry has children, its Children field will be true, and the children
// follow, terminated by an Entry with Tag 0.
type Reader struct {
	b            buf
	d            *Data
	err          error
	unit         int
	lastChildren bool   // .Children of last entry returned by Next
	lastSibling  Offset // .Val(AttrSibling) of last entry returned by Next
	cu           *Entry // current compilation unit
}

// Reader returns a new Reader for Data.
// The reader is positioned at byte offset 0 in the DWARF ``info'' section.
func (d *Data) Reader() *Reader {}

// AddressSize returns the size in bytes of addresses in the current compilation
// unit.
func (r *Reader) AddressSize() int {}

// ByteOrder returns the byte order in the current compilation unit.
func (r *Reader) ByteOrder() binary.ByteOrder {}

// Seek positions the Reader at offset off in the encoded entry stream.
// Offset 0 can be used to denote the first entry.
func (r *Reader) Seek(off Offset) {}

// Next reads the next entry from the encoded entry stream.
// It returns nil, nil when it reaches the end of the section.
// It returns an error if the current offset is invalid or the data at the
// offset cannot be decoded as a valid Entry.
func (r *Reader) Next() (*Entry, error) {}

// SkipChildren skips over the child entries associated with
// the last Entry returned by Next. If that Entry did not have
// children or Next has not been called, SkipChildren is a no-op.
func (r *Reader) SkipChildren() {}

// SeekPC returns the Entry for the compilation unit that includes pc,
// and positions the reader to read the children of that unit.  If pc
// is not covered by any unit, SeekPC returns ErrUnknownPC and the
// position of the reader is undefined.
//
// Because compilation units can describe multiple regions of the
// executable, in the worst case SeekPC must search through all the
// ranges in all the compilation units. Each call to SeekPC starts the
// search at the compilation unit of the last call, so in general
// looking up a series of PCs will be faster if they are sorted. If
// the caller wishes to do repeated fast PC lookups, it should build
// an appropriate index using the Ranges method.
func (r *Reader) SeekPC(pc uint64) (*Entry, error) {}

// Ranges returns the PC ranges covered by e, a slice of [low,high) pairs.
// Only some entry types, such as TagCompileUnit or TagSubprogram, have PC
// ranges; for others, this will return nil with no error.
func (d *Data) Ranges(e *Entry) ([][2]uint64, error) {}

// A LineReader reads a sequence of LineEntry structures from a DWARF
// "line" section for a single compilation unit. LineEntries occur in
// order of increasing PC and each LineEntry gives metadata for the
// instructions from that LineEntry's PC to just before the next
// LineEntry's PC. The last entry will have its EndSequence field set.
type LineReader struct {
	buf buf

	// Original .debug_line section data. Used by Seek.
	section []byte

	str     []byte // .debug_str
	lineStr []byte // .debug_line_str

	// Header information
	version              uint16
	addrsize             int
	segmentSelectorSize  int
	minInstructionLength int
	maxOpsPerInstruction int
	defaultIsStmt        bool
	lineBase             int
	lineRange            int
	opcodeBase           int
	opcodeLengths        []int
	directories          []string
	fileEntries          []*LineFile

	programOffset Offset // section offset of line number program
	endOffset     Offset // section offset of byte following program

	initialFileEntries int // initial length of fileEntries

	// Current line number program state machine registers
	state     LineEntry // public state
	fileIndex int       // private state
}

// A LineEntry is a row in a DWARF line table.
type LineEntry struct {
	// Address is the program-counter value of a machine
	// instruction generated by the compiler. This LineEntry
	// applies to each instruction from Address to just before the
	// Address of the next LineEntry.
	Address uint64

	// OpIndex is the index of an operation within a VLIW
	// instruction. The index of the first operation is 0. For
	// non-VLIW architectures, it will always be 0. Address and
	// OpIndex together form an operation pointer that can
	// reference any individual operation within the instruction
	// stream.
	OpIndex int

	// File is the source file corresponding to these
	// instructions.
	File *LineFile

	// Line is the source code line number corresponding to these
	// instructions. Lines are numbered beginning at 1. It may be
	// 0 if these instructions cannot be attributed to any source
	// line.
	Line int

	// Column is the column number within the source line of these
	// instructions. Columns are numbered beginning at 1. It may
	// be 0 to indicate the "left edge" of the line.
	Column int

	// IsStmt indicates that Address is a recommended breakpoint
	// location, such as the beginning of a line, statement, or a
	// distinct subpart of a statement.
	IsStmt bool

	// BasicBlock indicates that Address is the beginning of a
	// basic block.
	BasicBlock bool

	// PrologueEnd indicates that Address is one (of possibly
	// many) PCs where execution should be suspended for a
	// breakpoint on entry to the containing function.
	//
	// Added in DWARF 3.
	PrologueEnd bool

	// EpilogueBegin indicates that Address is one (of possibly
	// many) PCs where execution should be suspended for a
	// breakpoint on exit from this function.
	//
	// Added in DWARF 3.
	EpilogueBegin bool

	// ISA is the instruction set architecture for these
	// instructions. Possible ISA values should be defined by the
	// applicable ABI specification.
	//
	// Added in DWARF 3.
	ISA int

	// Discriminator is an arbitrary integer indicating the block
	// to which these instructions belong. It serves to
	// distinguish among multiple blocks that may all have with
	// the same source file, line, and column. Where only one
	// block exists for a given source position, it should be 0.
	//
	// Added in DWARF 3.
	Discriminator int

	// EndSequence indicates that Address is the first byte after
	// the end of a sequence of target machine instructions. If it
	// is set, only this and the Address field are meaningful. A
	// line number table may contain information for multiple
	// potentially disjoint instruction sequences. The last entry
	// in a line table should always have EndSequence set.
	EndSequence bool
}

// A LineFile is a source file referenced by a DWARF line table entry.
type LineFile struct {
	Name   string
	Mtime  uint64 // Implementation defined modification time, or 0 if unknown
	Length int    // File length, or 0 if unknown
}

// LineReader returns a new reader for the line table of compilation
// unit cu, which must be an Entry with tag TagCompileUnit.
//
// If this compilation unit has no line table, it returns nil, nil.
func (d *Data) LineReader(cu *Entry) (*LineReader, error) {}

// Next sets *entry to the next row in this line table and moves to
// the next row. If there are no more entries and the line table is
// properly terminated, it returns io.EOF.
//
// Rows are always in order of increasing entry.Address, but
// entry.Line may go forward or backward.
func (r *LineReader) Next(entry *LineEntry) error {}

// A LineReaderPos represents a position in a line table.
type LineReaderPos struct {
	// off is the current offset in the DWARF line section.
	off Offset
	// numFileEntries is the length of fileEntries.
	numFileEntries int
	// state and fileIndex are the statement machine state at
	// offset off.
	state     LineEntry
	fileIndex int
}

// Tell returns the current position in the line table.
func (r *LineReader) Tell() LineReaderPos {}

// Seek restores the line table reader to a position returned by Tell.
//
// The argument pos must have been returned by a call to Tell on this
// line table.
func (r *LineReader) Seek(pos LineReaderPos) {}

// Reset repositions the line table reader at the beginning of the
// line table.
func (r *LineReader) Reset() {}

// Files returns the file name table of this compilation unit as of
// the current position in the line table. The file name table may be
// referenced from attributes in this compilation unit such as
// AttrDeclFile.
//
// Entry 0 is always nil, since file index 0 represents "no file".
//
// The file name table of a compilation unit is not fixed. Files
// returns the file table as of the current position in the line
// table. This may contain more entries than the file table at an
// earlier position in the line table, though existing entries never
// change.
func (r *LineReader) Files() []*LineFile {}

// ErrUnknownPC is the error returned by LineReader.ScanPC when the
// seek PC is not covered by any entry in the line table.
var ErrUnknownPC = errors.New("ErrUnknownPC")

// SeekPC sets *entry to the LineEntry that includes pc and positions
// the reader on the next entry in the line table. If necessary, this
// will seek backwards to find pc.
//
// If pc is not covered by any entry in this line table, SeekPC
// returns ErrUnknownPC. In this case, *entry and the final seek
// position are unspecified.
//
// Note that DWARF line tables only permit sequential, forward scans.
// Hence, in the worst case, this takes time linear in the size of the
// line table. If the caller wishes to do repeated fast PC lookups, it
// should build an appropriate index of the line table.
func (r *LineReader) SeekPC(pc uint64, entry *LineEntry) error {}

func (i Tag) String() string {}

// A Type conventionally represents a pointer to any of the
// specific Type structures (CharType, StructType, etc.).
type Type interface {
	Common() *CommonType
	String() string
	Size() int64
}

// A CommonType holds fields common to multiple types.
// If a field is not known or not applicable for a given type,
// the zero value is used.
type CommonType struct {
	ByteSize int64  // size of value of this type, in bytes
	Name     string // name that can be used to refer to type
}

func (c *CommonType) Common() *CommonType {}

func (c *CommonType) Size() int64 {}

// Basic types

// A BasicType holds fields common to all basic types.
type BasicType struct {
	CommonType
	BitSize   int64
	BitOffset int64
}

func (b *BasicType) Basic() *BasicType {}

func (t *BasicType) String() string {}

// A CharType represents a signed character type.
type CharType struct {
	BasicType
}

// A UcharType represents an unsigned character type.
type UcharType struct {
	BasicType
}

// An IntType represents a signed integer type.
type IntType struct {
	BasicType
}

// A UintType represents an unsigned integer type.
type UintType struct {
	BasicType
}

// A FloatType represents a floating point type.
type FloatType struct {
	BasicType
}

// A ComplexType represents a complex floating point type.
type ComplexType struct {
	BasicType
}

// A BoolType represents a boolean type.
type BoolType struct {
	BasicType
}

// An AddrType represents a machine address type.
type AddrType struct {
	BasicType
}

// An UnspecifiedType represents an implicit, unknown, ambiguous or nonexistent type.
type UnspecifiedType struct {
	BasicType
}

// qualifiers

// A QualType represents a type that has the C/C++ "const", "restrict", or "volatile" qualifier.
type QualType struct {
	CommonType
	Qual string
	Type Type
}

func (t *QualType) String() string {}

func (t *QualType) Size() int64 {}

// An ArrayType represents a fixed size array type.
type ArrayType struct {
	CommonType
	Type          Type
	StrideBitSize int64 // if > 0, number of bits to hold each element
	Count         int64 // if == -1, an incomplete array, like char x[].
}

func (t *ArrayType) String() string {}

func (t *ArrayType) Size() int64 {}

// A VoidType represents the C void type.
type VoidType struct {
	CommonType
}

func (t *VoidType) String() string {}

// A PtrType represents a pointer type.
type PtrType struct {
	CommonType
	Type Type
}

func (t *PtrType) String() string {}

// A StructType represents a struct, union, or C++ class type.
type StructType struct {
	CommonType
	StructName string
	Kind       string // "struct", "union", or "class".
	Field      []*StructField
	Incomplete bool // if true, struct, union, class is declared but not defined
}

// A StructField represents a field in a struct, union, or C++ class type.
type StructField struct {
	Name       string
	Type       Type
	ByteOffset int64
	ByteSize   int64 // usually zero; use Type.Size() for normal fields
	BitOffset  int64 // within the ByteSize bytes at ByteOffset
	BitSize    int64 // zero if not a bit field
}

func (t *StructType) String() string {}

func (t *StructType) Defn() string {}

// An EnumType represents an enumerated type.
// The only indication of its native integer type is its ByteSize
// (inside CommonType).
type EnumType struct {
	CommonType
	EnumName string
	Val      []*EnumValue
}

// An EnumValue represents a single enumeration value.
type EnumValue struct {
	Name string
	Val  int64
}

func (t *EnumType) String() string {}

// A FuncType represents a function type.
type FuncType struct {
	CommonType
	ReturnType Type
	ParamType  []Type
}

func (t *FuncType) String() string {}

// A DotDotDotType represents the variadic ... function parameter.
type DotDotDotType struct {
	CommonType
}

func (t *DotDotDotType) String() string {}

// A TypedefType represents a named type.
type TypedefType struct {
	CommonType
	Type Type
}

func (t *TypedefType) String() string {}

func (t *TypedefType) Size() int64 {}

// An UnsupportedType is a placeholder returned in situations where we
// encounter a type that isn't supported.
type UnsupportedType struct {
	CommonType
	Tag Tag
}

func (t *UnsupportedType) String() string {}

// typeReader is used to read from either the info section or the
// types section.
type typeReader interface {
	Seek(Offset)
	Next() (*Entry, error)
	clone() typeReader
	offset() Offset
	// AddressSize returns the size in bytes of addresses in the current
	// compilation unit.
	AddressSize() int
}

// Type reads the type at off in the DWARF ``info'' section.
func (d *Data) Type(off Offset) (Type, error) {}
