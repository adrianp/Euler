import sys

from euler_util import read_triangle, triangle_max_sum


def main(*args, **kwargs):
    print triangle_max_sum(read_triangle("num_triangles/triangle_p067"))
    return 0

if __name__ == "__main__":
    sys.exit(main())
