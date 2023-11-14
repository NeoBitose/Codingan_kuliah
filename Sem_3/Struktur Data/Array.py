import ctypes
class Array :
   def __init__( self, ukuran ):
      assert ukuran > 0, "array harus memiliki elemen sebanyak > 0"
      self.ukuran = ukuran
      PyArrayType = ctypes.py_object * ukuran
      self.anggota = PyArrayType()
      self.isidata( None )

   def getlength( self ):
      return self.ukuran
   
   def getitem( self, index ):
      assert index >= 0 and index < self.getlength(), "out of range"
      return self.anggota[ index ]

   def setitem( self, index, value ):
      assert index >= 0 and index < banyakanggota(self), "out of range"
      self.anggota[index ] = value

   def isidata( self, value ):
      ukuran = self.getlength()
      for i in range(ukuran ) :
         self.anggota[i] = value