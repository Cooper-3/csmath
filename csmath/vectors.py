class Vectors:
    @staticmethod
    def create_Vector2(x, y):
        if not isinstance(x, (int, float)):
            raise ValueError(f"Invalid input for vector2 x value: {x}, make sure x and y are integers or floats!")
        elif not isinstance(y, (int, float)):
            raise ValueError(f"Invalid input for vector2 y value: {y}, make sure x and y are integers or floats!")
        else:
            vector2 = [x, y]
            return vector2

    @staticmethod
    def create_Vector3(x, y, z):
        if not isinstance(x, (int, float)):
            raise ValueError(f"Invalid input for vector3 x value: {x}, make sure x and y are integers or floats!")
        elif not isinstance(y, (int, float)):
            raise ValueError(f"Invalid input for vector3 y value: {y}, make sure x and y are integers or floats!")
        elif not isinstance(z, (int, float)):
            raise ValueError(f"Invalid input for vector3 z value: {z}, make sure x, y, and z are integers or floats!")
        else:
            vector3 = [x, y, z]
            return vector3

    @staticmethod
    def get_vector_type(vector, mode):
        if mode != 1:
            if mode == 0 and (len(vector) != 2 and len(vector) != 3):
                raise ValueError(f"Inputted vector is not valid: {vector} length: {len(vector)}")
            return None
        
        if len(vector) == 2:
            return "Vector2"
        elif len(vector) == 3:
            return "Vector3"
        else:
            if mode == 0:
                raise ValueError(f"Inputted vector is not valid: {vector} length: {len(vector)}")

    def edit_Vector(self, vector, axis, amount, mode=None):
        self.get_vector_type(vector, 0)
        
        if mode == 1:
            vector_temp = vector.copy()  # Create a copy of the vector
            if axis == "x":
                vector_temp[0] += amount  # Corrected index for 'x'
            elif axis == "y":
                vector_temp[1] += amount  # Corrected index for 'y'
            elif axis == "z":
                if len(vector_temp) == 3:
                    vector_temp[2] += amount  # 'z' exists only in 3D vectors
                else:
                    raise ValueError("Invalid axis 'z' for 2D vector.")
            return vector_temp
        else:
            if axis == "x":
                vector[0] += amount  # Corrected index for 'x'
            elif axis == "y":
                vector[1] += amount  # Corrected index for 'y'
            elif axis == "z":
                if len(vector) == 3:
                    vector[2] += amount  # 'z' exists only in 3D vectors
                else:
                    raise ValueError("Invalid axis 'z' for 2D vector.")
            return vector