def print_progress_bar(steps, total_steps):
    bar_length = 10
    progress = int(bar_length * (steps + 1) / total_steps)
    bar = '#' * progress + '-' * (bar_length - progress)
    print(f'[{bar}] {steps + 1}/{total_steps}', end='\r')
