from manim import *

class GabrielTrumpet(Scene):
    def construct(self):
        # 1. Criar os eixos
        axes = Axes(
            x_range=[0.5, 5, 1],  # Eixo x de 0.5 a 5
            y_range=[0, 2, 0.5],  # Eixo y de 0 a 2
            tips=True,
        ).add_coordinates()

        self.play(Create(axes))
        self.wait(1)

        # 2. Escrever o título "Trombeta de Torricelli"
        title = Text("Trombeta de Torricelli", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 3. Adicionar a equação f(x) = 1/x
        equation = Text("f(x) = 1/x")
        equation.next_to(title, DOWN)
        self.play(Write(equation))
        self.wait(2)

        # 4. Apagar o título e a equação
        self.play(FadeOut(title), FadeOut(equation))
        self.wait(1)

        # 5. Desenhar o gráfico da função
        graph = axes.plot(lambda x: 1 / x, x_range=[1, 5], color=BLUE)
        graph_label = axes.get_graph_label(graph, label="\\frac{1}{x}", x_val=4, direction=UP)
        self.play(Create(graph), Write(graph_label))
        self.wait(3)

        # 7. Demonstração da área infinita
        # Adicionando uma forma para representar a área infinita sob o gráfico
        area = axes.get_area(graph, x_range=[1, 5], color=BLUE, opacity=0.3)
        self.play(Create(area))
        self.wait(2)

        self.play(FadeOut(axes))
        self.wait(1)

        # 8. Mostrar a equação e sua resolução (Área)
        area_equation = MathTex(
            r"A = 2\pi \int_1^a \sqrt{1 + \left( \frac{-1}{x^2} \right)^2} \, dx > 2\pi \int_1^a \frac{dx}{x} = 2\pi \ln(a)"
        )
        area_equation.to_edge(UP)
        self.play(Write(area_equation))
        self.wait(2)

        # 9. Mostrar a resolução (Área)
        limit_area_equation = MathTex(
            r"\lim_{a \to \infty} A \geq \lim_{a \to \infty} 2\pi \ln(a) = \infty"
        )
        limit_area_equation.next_to(area_equation, DOWN)
        self.play(Write(limit_area_equation))
        self.wait(3)

        # 9.1. Apagar equação da área
        self.play(FadeOut(area_equation), FadeOut(limit_area_equation), FadeOut(area), FadeOut(graph), FadeOut(graph_label))
        self.wait(1)

        # 10. Demonstração do volume finito (representação de volume de um cone)
        volume_text = Text("Volume Finito", font_size=36)
        volume_text.to_edge(UP)
        self.play(Write(volume_text))
        self.wait(1)

        # 11. Mostrar a equação e sua resolução (Volume)
        volume_equation = MathTex(r"V = \pi \int_1^a \frac{1}{x} dx")
        volume_equation.next_to(volume_text, DOWN)
        self.play(Write(volume_equation))
        self.wait(3)

        # 12. Mostrar a equação com limite (como na imagem fornecida)
        limit_equation = MathTex(r"\lim_{a \to \infty} V = \lim_{a \to \infty} \pi \left( 1 - \frac{1}{a} \right) = \pi")
        limit_equation.next_to(volume_equation, DOWN)
        self.play(Write(limit_equation))
        self.wait(3)

        # 12.1 apaga equação do volume
        self.play(FadeOut(volume_equation), FadeOut(limit_equation), FadeOut(volume_text))
        self.wait(1)

        #---------------------------------------------------------------------------------------------------------------------#

        # 1. iniciando outro exemplo
        axes = Axes(
            x_range=[0.5, 5, 1],
            y_range=[0, 2, 0.5],
            tips=True,
        ).add_coordinates()

        self.play(Create(axes))
        self.wait(1)

        # 2. Criar paralelepípedos empilhados (3D)
        paralelepipedos = VGroup()
        for i in range(1, 6):
            # Definir altura proporcional a 1/x
            height = 1 / i
            # Largura será fixa, espessura em x, y e z
            width = 0.5
            depth = 0.2  # Espessura
            # Criar o paralelepípedo (caixa 3D)
            paralelepiped = Cube().scale([width, depth, height]).shift(RIGHT * i + UP * height / 2)
            paralelepipedos.add(paralelepiped)
        
        # 3. Animação dos paralelepípedos aparecendo
        self.play(LaggedStartMap(FadeIn, paralelepipedos, shift=UP))
        self.wait(2)

        # 4. Adicionar o título da área infinita
        area_text = Text("Área Infinita (Caixa com Paralelepípedos)", font_size=36)
        area_text.to_edge(UP)
        self.play(Write(area_text))
        self.wait(2)

        # 5. Transição para Volume Finito
        volume_text = Text("Volume Finito (Transformação para Cone)", font_size=36)
        volume_text.to_edge(UP)
        self.play(Transform(area_text, volume_text))
        self.wait(1)

        # 6. Criar o cone para representar o volume finito
        cone = Cone(height=5, base_radius=3, direction=UP, fill_color=BLUE, stroke_color=WHITE)
        cone.shift(RIGHT * 2)  # Ajustar posição do cone
        self.play(Transform(paralelepipedos, cone))
        self.wait(2)