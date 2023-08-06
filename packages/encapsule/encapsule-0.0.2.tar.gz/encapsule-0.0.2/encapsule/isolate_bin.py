# !!! This runs as SETUID=0 !!!
'''
SYSBIN=/system/bin

setuid -u 0 "$SYSBIN/.isolate"
PATH=$SYSBIN:$PATH

.isolate --post-context assets/Itham/services/component/query \
	--keyword=value arg1 arg2 arg3 \
	| wget 'https://network/channel/x' -x post


assets/Itham/services/component::
	def query():
		return 'text/json/dumps' \
			(mapping(arguments = args$(), \
				     keywords = keywords$()))

'''

import sys
import op

from json import loads as deserialize, dumps as serialize

from op.platform.path import CalledProcessError

from . import isolate_sys

publicName = hash

def invocation(argv = None):
	try: (options, output) = main(argv)
	except CalledProcessError as e:
		sys.stderr.write(e.stderrOutput)
		sys.exit(e.returncode)

		raise SystemError(f'Could not exit (returncode: {e.returncode})')


	if options.post_context:
		# XXX Shouldn't be json
		output = serialize(dict \
			(context = publicName \
				(isolate_sys.effectiveContextId()),
			 content = output))

	sys.stdout.write(output)


def buildOptions_parent(options):
	pass

def parseCmdln_subjective(argv):
	pass


class Component:
	@classmethod
	def Locate(self, options, name):
		return self(name, options, io.path \
			(options.component_root) \
				(*name.split('/')))

	def __init__(self, name, parentOptions, executable):
		self.name = name
		self.parentOptions = parentOptions
		self.executable = executable

	def pipeStringContext(options):
		# Subject Main.
		# Perform access check.

		# setuid pipe invocation

		isolate_sys.checkAccess(self)

		settings = dict(env = dict(TASK_ID = isolate_sys.generateNewTaskId())) \
				   if self.parentOptions.compartmentalize \
				   else dict()

		# XXX Todo: inside, set system-level 'current frame process id'
		# for whatever this task is.  Do this in a python context, when
		# exiting, reset to 'this frame process id.'
		return self.executable.pipeStringContext \
			(isolate_sys.effectiveContextId(), options,
			 segments = self.parentOptions.segments,
			 setTaskFrame_pid = isolate_sys.setTaskFrame_pid,
			 **settings)

def main(argv):
	((parentOptions, parentArgs), isoOptions) = \
		parseCmdln_subjective(argv)

	return (parentOptions, Component.Locate \
		(parentOptions, *parentArgs)	\
			.pipeStringContext(isoOptions))


class keyword:
	def __init__(self, name, value):
		self.name = name
		self.value = value

	def __str__(self):
		return f'--{name}={value}'

def exeCall(name, *args, **kwd)
	'''
	from encapsulate.isolate_bin import exeCallObject

	def run():
		try: return exeCallObject \
			('assets/Itham/services/component/query',
			 keyword('keyword', 'value'),
			 'arg1', 'arg2', 'arg3',
			 compartmentalize = True)

		except exeCallObject.error as e:
			return namespace(code = e.returncode,
							 error = e.stderrOutput,
							 output = e.stdOutput)

	'''

	return Component.Locate \
		(buildOptions_parent(kwd), name) \
			.pipeStringContext(' '.join(map(str, args)))

def exeCallObject(*args, **kwd):
	return deserialize(exeCall(*args, **kwd))

exeCallObject.error = CalledProcessError


if __name__ == '__main__':
	return main(sys.argv)
