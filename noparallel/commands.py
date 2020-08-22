from django.utils import timezone
from noparallel.models import CommandHistory

def noparallel():
    """
    This function is used as a decorator for commands. It prevents that the same command run again before the previous
    acurrence finishes.
    """

    def _method_wrapper(view_method):

        def _arguments_wrapper(request, *args, **kwargs):
            command = f'{request.__class__}'
            if CommandHistory.objects.filter(command=command, done_at__isnull=True).exists():
                print("Unfinished previous command found...")
                return
            else:
                CommandHistory.objects.filter(command=command).delete()
                CommandHistory.objects.create(
                    command=command
                )
                print("Running...")
                retval = view_method(request, *args, **kwargs)
                CommandHistory.objects.filter(
                    command=command, done_at__isnull=True).update(
                    done_at=timezone.now())
            return retval

        return _arguments_wrapper

    return _method_wrapper
