package fpp.compiler.codegen

import fpp.compiler.analysis._
import fpp.compiler.util._

/** Write an FPP type as C++ */
case class TypeCppWriter(
  /** CppWriterState */
  s: CppWriterState,
  /** Specific string type name */
  stringTypeName: Option[String] = None,
  /** List of namespace qualifiers for a string type */
  stringNamespaceNames: List[String] = Nil
) {

  private object NameVisitor extends TypeVisitor {

    override def absType(s: CppWriterState, t: Type.AbsType) =
      s.writeSymbol(Symbol.AbsType(t.node))

    override def array(s: CppWriterState, t: Type.Array) =
      s.writeSymbol(Symbol.Array(t.node))

    override def boolean(s: CppWriterState) = "bool"

    override def default(s: CppWriterState, t: Type) = throw new InternalError("visitor not defined")

    override def enumeration(s: CppWriterState, t: Type.Enum) =
      s.writeSymbol(Symbol.Enum(t.node))

    override def float(s: CppWriterState, t: Type.Float) = t.toString

    override def primitiveInt(s: CppWriterState, t: Type.PrimitiveInt) = t.toString

    override def string(s: CppWriterState, t: Type.String) = stringTypeName match {
      case Some(tn) => tn
      case None => StringCppWriter(s).getQualifiedClassName(t, stringNamespaceNames)
    }

    override def struct(s: CppWriterState, t: Type.Struct) =
      s.writeSymbol(Symbol.Struct(t.node))

    type In = CppWriterState

    type Out = String

  }

  /** Write the type */
  def write(t: Type): String = NameVisitor.ty(s, t)

}

object TypeCppWriter {

  /** Get the name of a type */
  def getName(
    s: CppWriterState,
    t: Type,
    stringTypeName: Option[String] = None,
    stringNamespaceNames: List[String] = Nil
  ): String =
    TypeCppWriter(s, stringTypeName, stringNamespaceNames).write(t)

}
