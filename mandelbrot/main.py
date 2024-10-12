from mandelbrot.configs import load_configs
from mandelbrot.draw import draw

def main():
    configs = load_configs()
    draw(configs)

if __name__ == "__main__":
    main()