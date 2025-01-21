import pygame

class View:
    """
    A class representing the main graphical interface for a pygame application.
    This class encapsulates a window and provides methods to start, run, and stop the application.
    """

    def __init__(self, width=800, height=600, title="Pygame Window"):
        """
        Initialize the View object.

        :param width: Width of the window (default is 800).
        :param height: Height of the window (default is 600).
        :param title: Title of the window (default is 'Pygame Window').
        """
        self.width = width
        self.height = height
        self.title = title
        self.running = False

        # Initialize pygame
        pygame.init()

        # Set up the display
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        # Clock for managing the frame rate
        self.clock = pygame.time.Clock()

    def start(self):
        """
        Start the application. Sets the running state to True and calls the run method.
        """
        self.running = True
        self.run()

    def run(self):
        """
        Main loop of the application. Handles events, updates the screen, and manages frame rate.
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

            # Fill the background with a color
            self.window.fill((255, 255, 255))  # White background

            # Draw sample shapes on the canvas
            self.draw_shapes()

            # Update the display
            pygame.display.flip()

            # Limit the frame rate to 60 FPS
            self.clock.tick(60)

    def stop(self):
        """
        Stop the application. Sets the running state to False and quits pygame.
        """
        self.running = False
        pygame.quit()

    def draw_shapes(self):
        """
        Draw sample shapes on the canvas in different colors.
        """
        # Draw a red rectangle
        pygame.draw.rect(self.window, (255, 0, 0), (50, 50, 200, 100))

        # Draw a blue circle
        pygame.draw.circle(self.window, (0, 0, 255), (400, 300), 50)

        # Draw a green line
        pygame.draw.line(self.window, (0, 255, 0), (600, 100), (700, 500), 5)

        # Draw a yellow ellipse
        pygame.draw.ellipse(self.window, (255, 255, 0), (300, 400, 150, 80))

# Example usage
if __name__ == "__main__":
    view = View()
    view.start()

