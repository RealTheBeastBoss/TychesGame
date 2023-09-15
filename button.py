from meta import *

class Button:
    def __init__(self, text, x_pos, y_pos, width, height):
        self.text = text
        self.xPos = x_pos
        self.yPos = y_pos
        self.width = width
        self.height = height
        self.draw()

    def draw(self):
        button_rect = pygame.rect.Rect((self.xPos, self.yPos), (self.width, self.height))
        if not self.check_hover():
            button_text = SMALL_FONT.render(self.text, True, ORANGE)
            pygame.draw.rect(WINDOW, BLUE, button_rect, 0, 5)
            pygame.draw.rect(WINDOW, ORANGE, button_rect, 3, 5)
        else:
            button_text = SMALL_FONT.render(self.text, True, BLUE)
            pygame.draw.rect(WINDOW, ORANGE, button_rect, 0, 5)
            pygame.draw.rect(WINDOW, BLUE, button_rect, 3, 5)
        text_width_offset = button_text.get_width() / 2
        text_height_offset = button_text.get_height() / 2
        WINDOW.blit(button_text, ((self.xPos + (self.width/2) - text_width_offset), (self.yPos + (self.height/2)) - text_height_offset))

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect((self.xPos, self.yPos), (self.width, self.height))
        if button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def check_click(self, left_mouse_released):
        button_rect = pygame.rect.Rect((self.xPos, self.yPos), (self.width, self.height))
        mouse_pos = pygame.mouse.get_pos()
        if left_mouse_released and button_rect.collidepoint(mouse_pos) and Meta.BUTTONS_ENABLED:
            pygame.time.set_timer(BUTTON_COOLDOWN_EVENT, 100, 1)
            Meta.BUTTONS_ENABLED = False
            return True
        return False