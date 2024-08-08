def draw_final_line(star_count):
    # Calculate the total number of stars to print in the final line
    total_stars = 5 + (int(star_count) - 1) * 2
    # Print the stars in a single line
    for _ in range(total_stars):
        print('* ', end='')
    print('\n')

def draw_final_lines(lines_count):
    # Print the final lines pattern for the specified number of lines
    for _ in range(lines_count):
        draw_final_line(lines_count)

def draw_upper_section(layers):
    space_count = layers * 2 + 2
    inner_space = 3
    for i in range(layers - 1):
        if i == 0:
            # Print the top-most single star line
            print(' ' * space_count + '*' + ' ' * space_count)
            space_count -= 2
        elif i == layers - 2:
            # Print the middle line with the number and stars
            print(' ' * space_count + '*' + ' ' * (inner_space // 2) + str(i + 2) + ' ' * (inner_space // 2) + '*')
            space_count -= 2
            inner_space += 4
        else:
            # Print the intermediate lines with two stars
            print(' ' * space_count + '*' + ' ' * inner_space + '*')
            space_count -= 2
            inner_space += 4

def create_pattern(value):
    # Check for valid input
    if value < 1:
        print('Please enter a positive number')
        return
    if value != int(value):
        print('Please enter an integer value')
        return

    # Generate the upper part of the pattern
    draw_upper_section(value)
    # Generate the final lines of the pattern
    draw_final_lines(value)

# Read user input
number = int(input("Enter a number: "))
create_pattern(number)
