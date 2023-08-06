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
from contextlib import contextmanager

from op.platform.path import CalledProcessError

from . import isolate_sys

__all__ = ['exeCall', 'exeCallObject', 'keyword']

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
	return namespace \
		(component_root = isolate_sys.ENCAPSULE_COMPONENTS_PATH,
		 compartmentalize = options.get('compartmentalize'),
		 segments = options.get('segments'),
		 post_context = options.get('post_context'))

def parseCmdln_subjective(argv):
	# Todo: wrong
	from optparse import OptionParser
	parser = OptionParser()
	parser.add_option('--post-context', action = 'store_true')

	(options, args) = parser.parse_args(argv)

	# isolate_bin invocations are always 'compartmentalized',
	# for now, because it represents an entry point.
	return ((buildOptions_parent \
				(namespace(post_context = options.post_context,
						   compartmentalize = True)),
			 (args[0],)), args[1:])


class Component:
	# This represents an invocation instance, so, we can
	# store invocation-specific data.

	@classmethod
	def Locate(self, options, name):
		return self(name, options, io.path \
			(options.component_root) \
				(*name.split('/')))

	def __init__(self, name, parentOptions, executable):
		self.name = name
		self.parentOptions = parentOptions
		self.executable = executable

	def newTaskId_env(self, **kwd):
		if self.parentOptions.compartmentalize:
			kwd['env'] = self.env_i = isolate_sys.generateNewTaskId_env()

		# _posixsubprocess-setuid: is this available on cygwin?
		kwd['user'] = isolate_sys.componentOwnerUser(self.name)

		return kwd

	@contextmanager
	def runContext(self, process):
		# grr
		with isolate_sys.setTaskFrame_pid \
			(self.env_i[isolate_sys.ENCAPSULE_TASK_ID_ENV],
			 process.pid, self.parentOptions.compartmentalize) as x:

			yield x

	def pipeStringContext(self, args):
		# Subject Main.
		# Perform access check.

		# setuid pipe invocation

		# XXX DISABLED FOR TESTING XXX
		# isolate_sys.checkAccessCurrentUser(self.name)

		settings = self.newTaskId_env(runContext = self.runContext)

		# XXX Todo: inside, set system-level 'current frame process id'
		# for whatever this task is.  Do this in a python context, when
		# exiting, reset to 'this frame process id.'
		# return self.executable.pipeStringContext \
		# 	(isolate_sys.effectiveContextId(), args,
		# 	 # segments = self.parentOptions.segments,
		# 	 # setTaskFrame_pid = isolate_sys.setTaskFrame_pid,
		# 	 **settings)

		# To work:
		# import pdb; pdb.set_trace()
		return self.executable.pipe \
			(*args, **settings) \
			.decode() # Why subprocess returns bytes stream,
					  # but sys.stdout is default opened str.

def main(argv):
	# import pdb; pdb.set_trace()
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

def exeCall(name, *args, **kwd):
	'''
	from encapsulate import exeCallObject, keyword

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
	invocation(sys.argv[1:])
	# invocation(sys.argv)
