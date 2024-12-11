import numpy as np
import math

def rotation(vector, x_rotation, y_rotation, z_rotation):
    x_rotation = (x_rotation / 180) * math.pi
    y_rotation = (y_rotation / 180) * math.pi
    z_rotation = (z_rotation / 180) * math.pi

    #print(x_rotation, y_rotation, z_rotation)
    
    xMatrix = np.array([[1,                     0,                      0, 0],
                        [0 , math.cos(x_rotation),  -math.sin(x_rotation), 0],
                        [0 , math.sin(x_rotation),   math.cos(x_rotation), 0],
                        [0 ,                    0,                      0, 1]])

    yMatrix = np.array([[math.cos(y_rotation),0,math.sin(y_rotation),0],
                        [0,1,0,0],
                        [-math.sin(y_rotation),0,math.cos(y_rotation),0],
                        [0,0,0,1]])

    zMatrix = np.array([[math.cos(z_rotation), -math.sin(z_rotation), 0, 0],
                        [math.sin(z_rotation), math.cos(z_rotation), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])


    afterX = np.dot(xMatrix, vector)
    afterY = np.dot(yMatrix, afterX)
    afterZ = np.dot(zMatrix, afterY)
    return afterZ

def translation(vector, x, y, z):
    return vector + np.array([x, y, z, 0])

def viewTransformation(vector, camX, camY, camZ):
    cam = np.array([[1, 0, 0, -camX],
              [0, 1, 0, -camY],
              [0, 0, 1, -camZ],
              [0, 0, 0,     1]])

    return np.dot(cam, vector)

def perspektiveTransformation(vector, right, top, near, far):
    perspective = np.array([[near/right, 0, 0, 0],
                            [0, near/top, 0, 0],
                            [0, 0, (-far + near) / (far-near), (-2*far*near) / (far-near)],
                            [0, 0,-1, 0]])
    
    return np.dot(perspective, vector)

def normalize(vector):
    return vector * (1 / vector[3])

def windowsSpace(vector, screenX, screenY):
    x = (vector[0] + 1) / 2 * screenX
    y = (vector[1] + 1) / 2 * screenY
    return np.array([x, y])

def threeD2Screen(vector, x_rotation, y_rotation, z_rotation, x_trans, y_trans, z_trans, cam_x, camY, camZ, right, top, near, far, screenX, screenY):
    afterRotation = rotation(vector, x_rotation, y_rotation, z_rotation)
    afterTranslation = translation(afterRotation, x_trans, y_trans, z_trans)
    afterView = viewTransformation(afterTranslation, cam_x, camY, camZ)
    afterPerspective = perspektiveTransformation(afterView, right, top, near, far)
    afterNormalizing = normalize(afterPerspective)
    windowCoords = windowsSpace(afterNormalizing, screenX, screenY)
    return windowCoords
    
#vector = np.array([3, 4, 2, 1])

#print(perspektiveTransformation(vector, 5, 5, 1, 20))



