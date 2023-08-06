package fpp.compiler.codegen

import fpp.compiler.analysis._
import fpp.compiler.ast._
import fpp.compiler.codegen._
import fpp.compiler.util._

/** Writes out C++ for component implementation templates */
case class ComponentImplWriter(
  s: CppWriterState,
  aNode: Ast.Annotated[AstNode[Ast.DefComponent]]
) extends ComponentCppWriterUtils(s, aNode) {

  private val fileName = ComputeCppFiles.FileNames.getComponentImpl(name)

  private val implClassName = name

  private val namespaceIdentList = s.getNamespaceIdentList(symbol)

  def write: CppDoc = {
    val includeGuard = s.includeGuardFromQualifiedName(symbol, fileName)
    CppWriter.createCppDoc(
      s"$name component implementation class",
      fileName,
      includeGuard,
      getMembers,
      s.toolName,
      "template.hpp",
      "template.cpp"
    )
  }

  private def getMembers: List[CppDoc.Member] = {
    val hppIncludes = getHppIncludes
    val cppIncludes = getCppIncludes
    val cls = classMember(
      None,
      implClassName,
      Some(s"public $className"),
      getClassMembers
    )
    List.concat(
      List(hppIncludes, cppIncludes),
      wrapInNamespaces(namespaceIdentList, List(cls))
    )
  }

  private def getHppIncludes: CppDoc.Member = {
    linesMember(
      addBlankPrefix(s.writeIncludeDirectives(List(symbol)).map(line)),
    )
  }

  private def getCppIncludes: CppDoc.Member = {
    val userHeaders = List(
      "FpConfig.hpp",
      s"${s.getRelativePath(fileName).toString}.hpp"
    )
    linesMember(
      addBlankPrefix(userHeaders.sorted.map(CppWriter.headerString).map(line)),
      CppDoc.Lines.Cpp
    )
  }

  private def getClassMembers: List[CppDoc.Class.Member] = {
    List.concat(
      getPublicMembers,
      getHandlers
    )
  }

  private def getPublicMembers: List[CppDoc.Class.Member] = {
    addAccessTagAndComment(
      "public",
      "Component construction and destruction",
      List(
        constructorClassMember(
          Some(s"Construct $implClassName object"),
          List(
            CppDoc.Function.Param(
              CppDoc.Type("const char* const"),
              "compName",
              Some("The component name")
            )
          ),
          List(s"$className(compName)"),
          Nil
        ),
        destructorClassMember(
          Some(s"Destroy $implClassName object"),
          Nil,
        )
      )
    )
  }

  private def getHandlers: List[CppDoc.Class.Member] = {
    List.concat(
      getPortHandlers(typedInputPorts),
      getPortHandlers(serialInputPorts),
      addAccessTagAndComment(
        "PRIVATE",
        s"Handler implementations for commands",
        nonParamCmds.map((opcode, cmd) =>
          functionClassMember(
            Some(
              addSeparatedString(
                s"Handler implementation for command ${cmd.getName}",
                AnnotationCppWriter.asStringOpt(cmd.aNode)
              )
            ),
            commandHandlerName(cmd.getName),
            List.concat(
              List(
                opcodeParam,
                cmdSeqParam,
              ),
              cmdParamMap(opcode)
            ),
            CppDoc.Type("void"),
            lines(
              s"""|// TODO
                  |this->cmdResponse_out(opCode, cmdSeq, Fw::CmdResponse::OK);
                  |"""
            )
          )
        )
      ),
      addAccessTagAndComment(
        "PRIVATE",
        s"Handler implementations for user-defined internal interfaces",
        internalPorts.map(p =>
          functionClassMember(
            Some(
              addSeparatedString(
                s"Handler implementation for ${p.getUnqualifiedName}",
                getPortComment(p)
              )
            ),
            internalInterfaceHandlerName(p.getUnqualifiedName),
            getPortFunctionParams(p),
            CppDoc.Type("void"),
            lines("// TODO")
          )
        )
      )
    )
  }

  private def getPortHandlers(ports: List[PortInstance]): List[CppDoc.Class.Member] = {
    addAccessTagAndComment(
      "PRIVATE",
      s"Handler implementations for user-defined ${getPortListTypeString(ports)} input ports",
      ports.map(p => {
        val todoMsg = getPortReturnType(p) match {
          case Some(_) => "// TODO return"
          case None => "// TODO"
        }

        functionClassMember(
          Some(
            addSeparatedString(
              s"Handler implementation for ${p.getUnqualifiedName}",
              getPortComment(p)
            )
          ),
          inputPortHandlerName(p.getUnqualifiedName),
          portNumParam :: getPortFunctionParams(p),
          getPortReturnTypeAsCppDocType(p),
          lines(todoMsg)
        )
      })
    )
  }

}
