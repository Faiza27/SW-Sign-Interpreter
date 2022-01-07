import json
SignDictionary = '''


{
    "words":[
        {
            "text": "a",
            "imgURL": "https://i.ibb.co/D9TXbyH/a.jpg"
        },
         {
            "text": "b",
            "imgURL": "https://i.ibb.co/bLBKzJs/b.jpg"
        },
         {
            "text": "c",
            "imgURL": "https://i.ibb.co/jM1nY8P/c.jpg"
        },
         {
            "text": "d",
            "imgURL": "https://i.ibb.co/yYhyMrG/d.jpg"
        },
         {
            "text": "e",
            "imgURL": "https://i.ibb.co/SwxX8tK/e.jpg"
        },
         {
            "text": "f",
            "imgURL": "https://i.ibb.co/gRgKKGc/f.jpg"
        },
         {
            "text": "g",
            "imgURL": "https://i.ibb.co/Fwz7V5g/g.jpg"
        },
         {
            "text": "h",
            "imgURL": "https://i.ibb.co/c30GydK/h.jpg"
        },
         {
            "text": "i",
            "imgURL": "https://i.ibb.co/KF5sTLp/i.jpg"
        },
         {
            "text": "j",
            "imgURL": "https://i.ibb.co/KbD6Lw7/j.jpg"
        },
         {
            "text": "k",
            "imgURL": "https://i.ibb.co/BKxppCM/k.jpg"
        },
         {
            "text": "l",
            "imgURL": "https://i.ibb.co/njS28rS/l.jpg"
        },
         {
            "text": "m",
            "imgURL": "https://i.ibb.co/FBGwq1z/m.jpg"
        },
         {
            "text": "n",
            "imgURL": "https://i.ibb.co/7SwCt5V/n.jpg"
        },
         {
            "text": "o",
            "imgURL": "https://i.ibb.co/Nydt0kP/o.jpg"
        },
         {
            "text": "p",
            "imgURL": "https://i.ibb.co/XCRGLgw/p.jpg"
        },
         {
            "text": "q",
            "imgURL": "https://i.ibb.co/Lzc2L8Q/q.jpg"
        },
         {
            "text": "r",
            "imgURL": "https://i.ibb.co/09yDrZc/r.jpg"
        },
         {
            "text": "s",
            "imgURL": "https://i.ibb.co/2FB2cK2/s.jpg"
        },
         {
            "text": "t",
            "imgURL": "https://i.ibb.co/mt9MyQh/t.jpg"
        },
         {
            "text": "u",
            "imgURL": "https://i.ibb.co/Y8QWcqx/u.jpg"
        },
         {
            "text": "v",
            "imgURL": "https://i.ibb.co/LxJrqYY/v.jpg"
        },
         {
            "text": "w",
            "imgURL": "https://i.ibb.co/djTBjZk/w.jpg"
        },
         {
            "text": "x",
            "imgURL": "https://i.ibb.co/zm6gGpz/x.jpg"
        },
         {
            "text": "y",
            "imgURL": "https://i.ibb.co/LpdTZRb/y.jpg"
        },
         {
            "text": "z",
            "imgURL": "https://i.ibb.co/x5spmYZ/z.jpg"
        }
    
    
    ]
}

'''


data= json.loads(SignDictionary)

print(data)
""" Dictionary type data"""
print(type(data))
"""List type data"""
print(type(data['words']))

for word in data['words']:
    print(word)
    print(word['text'])



