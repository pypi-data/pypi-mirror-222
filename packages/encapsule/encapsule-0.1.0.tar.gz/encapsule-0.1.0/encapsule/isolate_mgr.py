from . import isolate_sys

def main(argv = None):
    from optparse import OptionParser
    parser = OptionParser()

    (options, args) = parser.parse_args(argv)
    (command, *args) = args

    if command == 'orch':
        (subcmd, *args) = args

        if subcmd in ['tasks', 'ps', 'list']:
            for t in isolate_sys.orchObject_i:
                print(t.path.basename)

        elif subcmd in ['suspend', 'pause']:
            (name,) = args
            isolate_sys.suspendTask(name)

        elif subcmd in ['resume']:
            (name,) = args
            isolate_sys.resumeTask(name)

        elif subcmd in ['kill']:
            (name,) = args
            (frame,) = isolate_sys.orchObject_i.taskOf(name)
            frame.process.terminate()

    elif command == 'access':
        (subcmd, *args) = args

        if subcmd in ['grant']:
            # encapsule.isolate_mgr access grant op read services/x/bin
            (userId, access, name) = args
            isolate_sys.grantAccess(userId, name, access = access)

    elif command in ['owner', 'ownership']:
        (subcmd, *args) = args

        if subcmd in ['set']:
            # encapsule.isolate_mgr ownership set op services/x
            (userId, name) = args
            isolate_sys.setComponentOwner(name, userId)


if __name__ == '__main__':
    main()
