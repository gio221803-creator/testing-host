import turtle

def draw_rectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def main():
    screen = turtle.Screen()
    screen.title("Gambar Laptop dengan Python Turtle")
    t = turtle.Turtle()
    t.speed(3)

    # 1. Menggambar Layar (Bagian Atas)
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    draw_rectangle(t, 200, 130, "#2c3e50") # Bingkai luar

    t.penup()
    t.goto(-90, 10)
    t.pendown()
    draw_rectangle(t, 180, 110, "#3498db") # Layar LCD (biru)

    # 2. Menggambar Badan/Keyboard (Bagian Bawah)
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    
    # Membuat efek perspektif sederhana (trapesium)
    t.fillcolor("#7f8c8d")
    t.begin_fill()
    t.goto(-130, -60)
    t.goto(130, -60)
    t.goto(100, 0)
    t.goto(-100, 0)
    t.end_fill()

    # 3. Menggambar Touchpad
    t.penup()
    t.goto(-30, -50)
    t.pendown()
    draw_rectangle(t, 60, 30, "#95a5a6")

    # 4. Menambahkan Detail Tombol Keyboard (Garis-garis)
    t.penup()
    t.goto(-90, -15)
    t.setheading(0)
    t.pendown()
    for i in range(3):
        t.forward(180)
        t.penup()
        t.goto(-90 - (i*5), -15 - (i*10))
        t.pendown()

    t.hideturtle()
    print("Gambar selesai!")
    screen.mainloop()

if __name__ == "__main__":
    main()