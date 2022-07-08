Scale.default = "minor"

Clock.bpm = 160

d1 >> play("x-o(-=)xxo{o-}")

b1 >> bass([1,3,4], dur=[2,0.5,1], oct=3)

p1 >> pluck([1,3,7], sus=2, amp=0.5)
p1.every(4, "stutter")
p1.every(3, "reverse")
    
print(SynthDefs)

p2 >> pads([1,3], dur=[8], oct=4)

p1.stop()

Clock.clear()
