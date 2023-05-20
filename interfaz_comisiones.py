
class InterfazGrafica:

    def __init__(self):
        self.window = Tk()

        self.window.geometry("416x284")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=284,
            width=416,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            145.0,
            0.0,
            416.0,
            284.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            0.0,
            145.0,
            284.0,
            fill="#00404D",
            outline="")

        self.canvas.create_text(
            13.0,
            113.0,
            anchor="nw",
            text="Comisiones presenciales",
            fill="#FFFFFF",
            font=("InriaSans LightItalic", 10 * -1)
        )

        self.canvas.create_text(
            184.0,
            39.0,
            anchor="nw",
            text="Seleccione la matriz Productos/Canales:",
            fill="#002A33",
            font=("InriaSans Regular", 11 * -1)
        )

        self.canvas.create_text(
            211.0,
            100.0,
            anchor="nw",
            text="Grupo y columna de la matriz:",
            fill="#002A33",
            font=("InriaSans Regular", 11 * -1)
        )

        self.canvas.create_text(
            245.0,
            161.0,
            anchor="nw",
            text="Fecha de inicio:",
            fill="#002A33",
            font=("InriaSans Regular", 11 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            bg="#D9D9D9",
            relief="flat"
        )
        self.button_1.place(
            x=215.0,
            y=232.0,
            width=135.0,
            height=39.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        
        self.button_2 = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            bg="#D9D9D9",
            relief="flat"
        )
        self.button_2.place(
            x=269.0,
            y=67.0,
            width=30.0,
            height=33.0
        )

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            72.0,
            50.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            72.0,
            89.0,
            image=self.image_image_2
        )

        self.canvas.create_rectangle(
            11.0,
            106.0,
            131.0,
            108.0,
            fill="#FFFFFF",
            outline="")
        self.window.resizable(False, False)
        self.window.mainloop()