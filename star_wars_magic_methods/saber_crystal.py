class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        self.color = (self.red, self.green, self.blue)
    
    def __eq__(self, other):
        return self.color == other.color
 
    def __add__(self, other):
        # Solution #1: Check data type of 'other'
        # if type(other) is tuple:
        #     result = tuple(sum(x) for x in zip(self.color, other))
        # else:
        #     result = tuple(sum(x) for x in zip(self.color, other.color))
        # return SaberCrystal(color=result)

        # Solution #2: Check whether 'other' is an instance of SaberCrystal
        if isinstance(other, SaberCrystal):
            my_zip = zip(self.color, other.color)
        else:
            my_zip = zip(self.color, other)
        
        result = [sum(x) for x in my_zip]

        # for loop approach
        # new_result = []
        # for i in result:
        #     if i > 255:
        #         new_result.append(255)
        #     else:
        #         new_result.append(i)

        # List comprehension approach: expression -> if-else condition -> iterable 
        new_result = [255 if i > 255 else i for i in result]
        return SaberCrystal(color = tuple(new_result))

    def __sub__(self, other):
        if isinstance(other, SaberCrystal):
            my_zip = zip(self.color, other.color)
        else:
            my_zip = zip(self.color, other)
       
        result = [abs(x-y) for x, y in my_zip]
        new_result = [255 if i > 255 else i for i in result]
        return SaberCrystal(color = tuple(new_result))

    def __contains__(self, other):       
        if isinstance(other, SaberCrystal):
            my_zip = zip(self.color, other.color)
        else:
            my_zip = zip(self.color, other)
        
        checklist = [True for x, y in my_zip if x == y and x != 0]
        if True in checklist:
            return True
        # else:
        #     return False
        