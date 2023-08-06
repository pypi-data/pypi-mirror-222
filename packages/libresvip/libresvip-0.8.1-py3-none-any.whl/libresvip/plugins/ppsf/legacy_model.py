from construct import (
    Byte,
    Bytes,
    BytesInteger,
    Const,
    GreedyRange,
    Int16ul,
    LazyBound,
    PascalString,
    Prefixed,
    PrefixedArray,
    Struct,
    Switch,
    this,
)

Int32ul = BytesInteger(4, swapped=True)

PpsfChunk = Struct(
    "magic" / Bytes(4),
    "size" / Int32ul,
    "data" / Switch(
        this.magic,
        {
            b"PLGS": GreedyRange(PrefixedArray(
                Byte, LazyBound(lambda: PpsfChunk)
            ))
        },
        default=Bytes(this.size)
    ),
)

PpsfLegacyProject = Struct(
    "magic" / Const(b"PPSF"),
    "body"
    / Prefixed(
        Int32ul,
        Struct(
            "version" / PascalString(Int16ul, "utf8"),
            "chunks" / GreedyRange(PpsfChunk),
        ),
    ),
)
