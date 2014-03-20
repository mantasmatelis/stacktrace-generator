#!/usr/bin/python

import lldb
import os

debugger = lldb.SBDebugger.Create()
debugger.SetAsync(False)

target = debugger.CreateTargetWithFileAndArch("a.out", lldb.LLDB_ARCH_DEFAULT)

if not target:
	print "Could not set target"
	exit(1)

process = target.LaunchSimple(None, None, os.getcwd())

# Make sure the launch went ok
if not process:
    print "Could not launch process"
    exit(1)

state = process.GetState()

if state != lldb.eStateStopped:
    print "Process not stopped. (for some reason)"
    exit(1)

thread = process.GetThreadAtIndex(0)
if not thread:
    print "Could not get thread"
    exit(1)

for i in xrange(thread.GetNumFrames()):
    frame = thread.GetFrameAtIndex(i)
    next_frame = thread.GetFrameAtIndex(i + 1)
    if frame:
        function = frame.GetFunction()
        next_function = next_frame.GetFunction()
        if function:
            print "========================="
            print function.name + ":"
            
            param = frame.GetVariables(True, False, False, True)
            local = frame.GetVariables(False, True, False, True)

            for elem in param:
                print "  " + elem.GetName() + ": " + elem.GetValue()

            for elem in local:
                print "  " + elem.GetName() + ": " + elem.GetValue()

            if next_function:
                retfn = next_function.name + ":"
                retline = next_frame.line_entry.ling
            else:
                retfn = ""
                retline = "OS"
            print "return addr: " + str(retfn) + str(retline)
        else:
            # Print the trailing set of equals
            print "========================="
            break
