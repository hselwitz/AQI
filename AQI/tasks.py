from background_task import background


@background(schedule=5)
def call_main_logger():
    print('g4')
