import pygame



# Inicializar Pygame

pygame.init()



# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie

width = 800

height = 600

surface = pygame.display.set_mode((width, height))

background_color = (10, 10, 10)

surface.fill(background_color)



# Establecer el tamaño de los píxeles

pixel_size = 1



# Establecer el color de las líneas

line_color = (255, 120, 10)



def draw_square():

    x = int(input("Ingrese la posición en X del cuadrado: "))

    y = int(input("Ingrese la posición en Y del cuadrado: "))

    size = int(input("Ingrese el tamaño de los lados del cuadrado: "))

    pygame.draw.rect(surface, line_color, (x, y, size, size), pixel_size)

    pygame.display.flip()



def draw_circle():

    x = int(input("Ingrese la posición en X del círculo: "))

    y = int(input("Ingrese la posición en Y del círculo: "))

    radius = int(input("Ingrese el radio del círculo: "))

    pygame.draw.circle(surface, line_color, (x, y), radius, pixel_size)

    pygame.display.flip()



def draw_rectangle():

    x = int(input("Ingrese la posición en X del rectángulo: "))

    y = int(input("Ingrese la posición en Y del rectángulo: "))

    width = int(input("Ingrese el ancho del rectángulo: "))

    height = int(input("Ingrese la altura del rectángulo: "))

    pygame.draw.rect(surface, line_color, (x, y, width, height), pixel_size)

    pygame.display.flip()



def draw_line():

    x1 = int(input("Ingrese la posición en X del punto A: "))

    y1 = int(input("Ingrese la posición en Y del punto A: "))

    x2 = int(input("Ingrese la posición en X del punto B: "))

    y2 = int(input("Ingrese la posición en Y del punto B: "))

    pygame.draw.line(surface, line_color, (x1, y1), (x2, y2), pixel_size)

    pygame.display.flip()



def draw_triangle_isosceles():

    x = int(input("Ingrese la posición en X del triángulo: "))

    y = int(input("Ingrese la posición en Y del triángulo: "))

    side = int(input("Ingrese el tamaño de los lados del triángulo: "))

    pygame.draw.polygon(surface, line_color, [(x, y), (x + side, y), (x + side / 2, y - side)], pixel_size)

    pygame.display.flip()



def draw_triangle_equilateral():

    x = int(input("Ingrese la posición en X del triángulo: "))

    y = int(input("Ingrese la posición en Y del triángulo: "))

    side = int(input("Ingrese el tamaño de los lados del triángulo: "))

    height = side * 0.866

    pygame.draw.polygon(surface, line_color, [(x, y), (x + side, y), (x + side / 2, y - height)], pixel_size)

    pygame.display.flip()



def draw_triangle_scalene():

    x1 = int(input("Ingrese la posición en X del punto A: "))

    y1 = int(input("Ingrese la posición en Y del punto A: "))

    x2 = int(input("Ingrese la posición en X del punto B: "))

    y2 = int(input("Ingrese la posición en Y del punto B: "))

    x3 = int(input("Ingrese la posición en X del punto C: "))

    y3 = int(input("Ingrese la posición en Y del punto C: "))

    pygame.draw.polygon(surface, line_color, [(x1, y1), (x2, y2), (x3, y3)], pixel_size)

    pygame.display.flip()



def change_background():

    option = input("SELECCIONE UN COLOR PARA EL FONDO:\n1. Negro\n2. Blanco\n3. Rojo\n4. Morado\nOpción: ")

    if option == "1":

        surface.fill((0, 0, 0))

    elif option == "2":

        surface.fill((255, 255, 255))

    elif option == "3":

        surface.fill((255, 0, 0))

    elif option == "4":

        surface.fill((128, 0, 128))

    else:

        print("Opción inválida. No se cambió el color del fondo.")

    pygame.display.flip()



def change_line_color():

    option = input("Seleccione un color para las líneas:\n1. Negro\n2. Morado\n3. Verde\n4. Blanco\nOpción: ")

    if option == "1":

        global line_color

        line_color = (0, 0, 0)

    elif option == "2":

        line_color = (128, 0, 128)

    elif option == "3":

        line_color = (0, 255, 0)

    elif option == "4":

        line_color = (255, 255, 255)

    else:

        print("Opción inválida. No se cambió el color de las líneas.")



def change_pixel_size():

    global pixel_size

    pixel_size = int(input("Ingrese el tamaño de los píxeles: "))



def show_draw_menu():

    print("--MENU PARA DIBUJAR--")

    print("1. CUADRADO")

    print("2. CIRCULO")

    print("3. RECTANGULO")

    print("4. LINEAS")

    print("5. TRIANGULOS")

    print("6. COLOR DEL FONDO")

    print("7. COLOR DE LAS LINEAS")

    print("8. TAMAÑO DE PIXEL DE LINEAS")

    print("9. Volver al menú principal")



def show_help():

    print("COLORES COMPATIBLES EN LAS LINEAS:")

    print("1. NEGRO")

    print("2. MORADO")

    print("3. VERDE")

    print("4. BLANCO")

    print()

    print("Colores compatibles para el fondo:")

    print("1. NEGRO")

    print("2. BLANCO")

    print("3. ROJO")

    print("4. MORADO")



def show_main_menu():

    print("--MENU PRINCIPAL--")

    print("1. DIBUJAR")

    print("2. HELP")

    print("3. EXIT")



# Esperar a que el usuario cierre la ventana

while True:

    show_main_menu()

    cmd = input("SELECCIONE UNA OPCION: ")

    if cmd == "1":

        while True:

            show_draw_menu()

            draw_cmd = input("SELECCIONE UNA OPCION PARA DIBUJO: ")

            if draw_cmd == "1":

                draw_square()

            elif draw_cmd == "2":

                draw_circle()

            elif draw_cmd == "3":

                draw_rectangle()

            elif draw_cmd == "4":

                draw_line()

            elif draw_cmd == "5":

                while True:

                    print("1. TRIANGULO ISOSCELES")

                    print("2. TRIANGULO EQUILATERO")

                    print("3. TRIANGULO ESCALENO")

                    print("4. Volver al menú anterior")

                    triangle_cmd = input("SELECCIONE UNA OPCION DE TRIANGULO: ")

                    if triangle_cmd == "1":

                        draw_triangle_isosceles()

                    elif triangle_cmd == "2":

                        draw_triangle_equilateral()

                    elif triangle_cmd == "3":

                        draw_triangle_scalene()

                    elif triangle_cmd == "4":

                        break

                    else:

                        print("OPCION INVALIDA SELECCIONE UNA NUEVA")

            elif draw_cmd == "6":

                change_background()

            elif draw_cmd == "7":

                change_line_color()

            elif draw_cmd == "8":

                change_pixel_size()

            elif draw_cmd == "9":

                break

            else:

                print("OPCION INVALDIA SELEECIONE UNA CORRECTA.")

    elif cmd == "2":

        show_help()

    elif cmd == "3":

        break

    else:

        print("OPCION INVALDIA SELECCIONE UNA NUEVA.")



# Salir de Pygame

pygame.quit()
