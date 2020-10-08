import numpy 


array_out = numpy.array([2658.0 , 1.0 , 2.0] , dtype=int )
numpy.savetxt("test.csv", array_out, delimiter="," , newline='\n' , fmt='%10.5f')