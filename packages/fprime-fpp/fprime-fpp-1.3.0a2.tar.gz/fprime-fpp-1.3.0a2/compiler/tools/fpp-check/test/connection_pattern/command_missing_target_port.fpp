module Fw {
  port Cmd
  port CmdReg
  port CmdResponse
}
module M {
  passive component Commands {
    sync input port cmdRegIn: Fw.CmdReg
    output port cmdOut: Fw.Cmd
    sync input port cmdResponseIn: Fw.CmdResponse
  }
  passive component C {
    command recv port cmdIn
    command resp port cmdResponseOut
  }
  instance commands: Commands base id 0x100
  instance c: C base id 0x100
  topology T {
    instance commands
    instance c
    command connections instance commands { c }
  }
}
