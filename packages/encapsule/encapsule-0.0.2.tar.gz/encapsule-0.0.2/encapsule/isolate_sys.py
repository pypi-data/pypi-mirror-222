from os import getuid as effectiveContextId, kill as processKill
from signal import SIGSTOP, SIGCONT


def setTaskFrame_pid(pid):
	pass

def generateNewTaskId():
	pass

def pidOf_taskFrame(taskId):
	pass


def suspendTask(taskId):
	return processKill(pidOf_taskFrame(taskId), SIGSTOP)
def resumeTask(taskId):
	return processKill(pidOf_taskFrame(taskId), SIGCONT)


class NoAccessException(Exception):
	pass

def checkAccess(component):
	if [component.name, 'read'] in _active_permissions[effectiveContextId()]:
		return True

	raise NoAccessException
