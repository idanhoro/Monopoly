import pygame


# TODO:ADD RADO BUTTEM

class effects:
    class GeneralEffects:
        def __init__(self, color=(0, 0, 0), thickness=5):
            self.color = color
            self.thickness = thickness

    class shadow(GeneralEffects):
        def __init__(self, color=(0, 0, 0), thickness=5):
            super().__init__(color, thickness)

        def apply(self, display, image, rect):
            mask = pygame.mask.from_surface(image)
            mask_surface = mask.to_surface(setcolor=self.color)
            mask_surface.set_colorkey((0, 0, 0))
            rect.center = rect.center[0] - self.thickness, rect.center[1] - self.thickness
            display.blit(mask_surface, rect)

    class bump(GeneralEffects):
        def __init__(self, color=(0, 0, 0), thickness=5):
            super().__init__(color, thickness)

        def apply(self, display, image, rect):
            mask = pygame.mask.from_surface(image)
            mask_surface = mask.to_surface(setcolor=self.color)
            mask_surface.set_colorkey((0, 0, 0))
            for i in range(self.thickness):
                rect.center = rect.center[0] + 1, rect.center[1]
                display.blit(mask_surface, rect)

    class blit_outline(GeneralEffects):
        def __init__(self, color=(0, 0, 0), thickness=5):
            super().__init__(color, thickness)

        def apply(self, display, image, rect):
            mask = pygame.mask.from_surface(image)
            mask_surface = mask.to_surface(setcolor=self.color)
            mask_surface.set_colorkey((0, 0, 0))
            for i in range(self.thickness):
                rect2 = rect.copy()
                rect2.center = rect2.center[0] + i, rect2.center[1]
                display.blit(mask_surface, rect2)
                rect2 = rect.copy()
                rect2.center = rect2.center[0], rect2.center[1] + i
                display.blit(mask_surface, rect2)
                rect2.center = rect2.center[0] - i, rect2.center[1]
                display.blit(mask_surface, rect2)
                rect2 = rect.copy()
                rect2.center = rect2.center[0], rect2.center[1] - i
                display.blit(mask_surface, rect2)


class Font:
    class style:  # TODO: add style
        def __init__(self, text, font_path='fonts/comic.ttf', font_size=30, font_color=(0, 0, 0),
                     highlight_color=(0, 0, 255), effects=None):
            self.font = pygame.font.Font(font_path, font_size)
            self.font_color = font_color
            self.highlight_color = highlight_color
            self.effects = effects

    def __init__(self, text, font_path='fonts/comic.ttf', font_size=30, font_color=(0, 0, 0),
                 highlight_color=(0, 0, 255), effects=None):
        self.text = text
        self.font = pygame.font.Font(font_path, font_size)
        self.font_color = font_color
        self.highlight_color = highlight_color
        self.effects = effects


class GeneralButton:
    def get_img_rect(self, menu, index: (int, int), highlight: bool):
        if highlight and self.font.highlight_color is not None:
            color = self.font.highlight_color
        else:
            color = self.font.font_color
        render_font = self.font.font.render(self.font.text, True, color)
        text_rect = render_font.get_rect()
        text_rect.center = (menu.offset[0] + menu.gap[0] * index[0], menu.offset[1] + menu.gap[1] * index[1])
        return render_font, text_rect

    def handle_click(self, menu):
        pass

    def handle_key(self, key):
        pass

    def render(self, menu, index, x, y):
        render_font, text_rect = self.get_img_rect(menu, index, False)
        if text_rect.collidepoint(x, y):
            render_font, text_rect = self.get_img_rect(menu, index, True)
            if self.font.effects is not None:
                self.font.effects.apply(menu.display, render_font, text_rect)
            if menu.click:
                menu.click = False
                self.handle_click()
        menu.display.blit(render_font, text_rect)


class Button(GeneralButton):
    def __init__(self, font: Font, function, arguments: dict = {}):
        self.font = font
        self.function = function
        self.arguments = arguments

    def handle_click(self):
        self.function(**self.arguments)


class BackButton(GeneralButton):
    def __init__(self, font: Font):
        self.font = font

    def render(self, menu, index, x, y):
        render_font, text_rect = self.get_img_rect(menu, index, False)
        if text_rect.collidepoint(x, y):
            render_font, text_rect = self.get_img_rect(menu, index, True)
            if self.font.effects is not None:
                self.font.effects.apply(menu.display, render_font, text_rect)
            if menu.click:
                menu.click = False
                menu.running = False
        menu.display.blit(render_font, text_rect)


class Header(GeneralButton):
    def __init__(self, font: Font):
        self.font = font

    def render(self, menu, index, x, y):
        render_font, text_rect = self.get_img_rect(menu, index, False)
        self.handle_key(menu.event_key)
        menu.display.blit(render_font, text_rect)


class RoundRobin(GeneralButton):
    def __init__(self, options: list[(Font, dict)], function, effect=None, first_stat=0, text: str = ""):
        self.font = options[first_stat][0]
        self.options = options
        self.function = function
        self.current = first_stat
        self.text = text
        self.effect = effect

    def handle_click(self):
        self.current = (self.current + 1) % len(self.options)
        self.function(**self.options[self.current][1])
        self.font = self.options[self.current][0]

    def render(self, menu, index, x, y):
        render_font, text_rect = self.get_img_rect(menu, index, False)
        if text_rect.collidepoint(x, y):
            render_font, text_rect = self.get_img_rect(menu, index, True)
            if self.font.effects is not None:
                self.font.effects.apply(menu.display, render_font, text_rect)
            if menu.click:
                menu.click = False
                self.handle_click()
        menu.display.blit(render_font, text_rect)


class Bar(GeneralButton):
    def __init__(self, font: Font, max_range: int, function, arguments: list[dict] = None, effect=None, on_bar="▪",
                 off_bar="▫",
                 left="<", right=">"):
        if arguments is None:
            arguments = [{} for _ in range(max_range + 1)]
        if len(arguments) <= max_range:
            raise Exception(f'The arguments list size mast be {max_range + 1}')
        self.font = font
        self.max_range = max_range
        self.current = max_range // 2
        self.function = function
        self.arguments = arguments
        self.effect = effect
        self.left = left
        self.right = right
        self.on_bar = on_bar
        self.off_bar = off_bar
        self.text_size = self.font.font.render(self.font.text, True, self.font.font_color).get_rect().size[0]
        self.left_size = self.font.font.render(self.left, True, self.font.font_color).get_rect().size[0]
        self.right_size = self.font.font.render(self.right, True, self.font.font_color).get_rect().size[0]
        self.on_bar_size = self.font.font.render(self.on_bar, True, self.font.font_color).get_rect().size[0]
        self.off_bar_size = self.font.font.render(self.off_bar, True, self.font.font_color).get_rect().size[0]

    def get_img_rect(self, menu, index: (int, int), highlight: bool):
        if highlight:
            color = self.font.highlight_color
        else:
            color = self.font.font_color
        render_font = self.font.font.render(self.font.text + self.left + self.on_bar * self.current + self.off_bar * (
                self.max_range - self.current) + self.right, True, color)
        text_rect = render_font.get_rect()
        text_rect.center = (menu.offset[0], menu.offset[1] + menu.gap[1] * index[1])
        return render_font, text_rect

    def handle_click(self, text_rect: int, mouse_ops: int):
        offset = mouse_ops - text_rect
        if (lim := self.text_size) < offset < lim + self.left_size and self.current > 0:
            self.current -= 1
        elif (lim := lim + self.left_size) < offset < lim + self.on_bar_size * self.current:
            self.current = (offset - lim) // self.on_bar_size + 1
        elif (lim := lim + + self.on_bar_size * self.current) < offset < lim + self.off_bar_size * (
                self.max_range - self.current):
            self.current = self.current + (offset - lim) // self.off_bar_size + 1
        elif lim + self.off_bar_size * (self.max_range - self.current) < offset and self.current < self.max_range:
            self.current += 1
        self.function(**self.arguments[self.current])
        return True

    def render(self, menu, index, x, y):
        render_font, text_rect = self.get_img_rect(menu, index, False)
        if text_rect.collidepoint(x, y):
            render_font, text_rect = self.get_img_rect(menu, index, True)
            if self.font.effects is not None:
                self.font.effects.apply(menu.display, render_font, text_rect)
            if menu.click:
                menu.click = False
                self.handle_click(text_rect.x, x)
        menu.display.blit(render_font, text_rect)


class InputBox(GeneralButton):
    def __init__(self, font: Font, function, text_arguments: list, arguments={}, effect=None, default: str = ""):
        self.font = font
        self.text = default
        self.active = False
        self.function = function
        self.arguments = arguments
        self.text_arguments = text_arguments
        self.effect = effect

    def handle_click(self):
        self.active = not self.active
        return True

    def get_img_rect(self, menu, index: (int, int), highlight: bool):
        if highlight:
            color = self.font.highlight_color
        else:
            color = self.font.font_color
        render_font = self.font.font.render(self.font.text + self.text, True, color)
        text_rect = render_font.get_rect()
        text_rect.center = (menu.offset[0], menu.offset[1] + menu.gap[1] * index[1])
        return render_font, text_rect

    def handle_key(self, event):
        if self.active and event is not None:
            if event.key == pygame.K_RETURN:
                for key in self.text_arguments:
                    self.arguments[key] = self.text
                self.function(**self.arguments)
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def render(self, menu, index, x, y):
        if self.active:
            render_font, text_rect = self.get_img_rect(menu, index, True)
        else:
            render_font, text_rect = self.get_img_rect(menu, index, False)
        if text_rect.collidepoint(x, y):
            render_font, text_rect = self.get_img_rect(menu, index, True)
            if self.font.effects is not None:
                self.font.effects.apply(menu.display, render_font, text_rect)
            if menu.click:
                menu.click = False
                self.handle_click()
        self.handle_key(menu.event_key)
        menu.display.blit(render_font, text_rect)


class Image(GeneralButton):
    def __init__(self, image: pygame.image, function, arguments: dict = {}, effect=None, disable=False,
                 disable_effect=None):
        self.image = image
        self.function = function
        self.arguments = arguments
        self.effect = effect
        self.disable_effect = disable_effect
        self.disable = disable

    def get_img_rect(self, menu, index: (int, int), highlight: bool):
        ract = self.image.get_rect(
            center=(menu.offset[0] + menu.gap[0] * index[0], menu.offset[1] + menu.gap[1] * index[1]))
        return self.image, ract

    def handle_click(self):
        self.function(**self.arguments)
        return True

    def render(self, menu, index, x, y):
        render_font, text_rect = self.get_img_rect(menu, index, False)
        if self.disable and self.disable_effect:
            self.disable_effect.apply(menu.display, render_font, text_rect)
            return
        if text_rect.collidepoint(x, y):
            if self.effect is not None:
                self.effect.apply(menu.display, render_font, text_rect)
            if menu.click:
                menu.click = False
                self.handle_click()
        menu.display.blit(render_font, text_rect)


class RadioButton(GeneralButton):
    def __init__(self, font: Font, function, arguments: dict = {}, group: int = 1):
        self.font = font
        self.function = function
        self.arguments = arguments
        self.group = group
        self.active = False

    def render(self, menu, index, x, y):
        if self.active:
            render_font, text_rect = self.get_img_rect(menu, index, True)
            if self.font.effects is not None:
                self.font.effects.apply(menu.display, render_font, text_rect)
        else:
            render_font, text_rect = self.get_img_rect(menu, index, False)
        if text_rect.collidepoint(x, y):
            render_font, text_rect = self.get_img_rect(menu, index, True)
            if self.font.effects is not None:
                self.font.effects.apply(menu.display, render_font, text_rect)
            if menu.click:
                menu.click = False
                self.handle_click(menu)
        menu.display.blit(render_font, text_rect)

    def handle_click(self, menu):
        self.function(**self.arguments)
        for line in menu.buttons:
            for button in line:
                if isinstance(button, RadioButton) and self.group == button.group:
                    button.active = False
        self.active = True


class Menu:
    def __init__(self, display: pygame.display, buttons: list[list[Button, RoundRobin, BackButton]],
                 offset: (int, int), gap: (int, int), background_color: (int, int, int) = None,
                 background_image: str = None):
        self.display = display
        self.buttons = buttons
        self.background_color = background_color
        self.offset = offset
        self.gap = gap
        self.running = True
        self.click = False
        self.event_key = None
        if background_image is not None:
            display_Info = pygame.display.Info()
            background_image = pygame.image.load(background_image)
            background_image = pygame.transform.scale(background_image,
                                                      (display_Info.current_w, display_Info.current_h))
        self.background_image = background_image

    def background(self):
        if self.background_color is not None:
            self.display.fill(self.background_color)
        if self.background_image is not None:
            self.display.blit(self.background_image, (0, 0))

    def event_loop(self):
        self.event_key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.click = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                self.event_key = event

    def render(self):
        self.running = True
        while self.running:
            self.event_loop()
            self.background()
            x, y = pygame.mouse.get_pos()
            for index_line, line in enumerate(self.buttons):
                for index_row, button in enumerate(line):
                    index = (index_row - (len(line) / 2) + 0.5, index_line)
                    button.render(self, index, x, y)
            pygame.display.flip()
            pygame.display.update()
