import pprint
def display_availability_table ( availability_table, output_file ) :

   # Create the text file
   text_file = open( output_file , "w" )
   text_file.close()
   
   # Get the size of array
   linebreak = " ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
   numOfDays = len( availability_table )
   numOfHours = len( availability_table[0] )
   numOfAmbulances = len( availability_table[0][0] )

   for i in range ( numOfDays ) :

      '''
         --------------------------------------------------
         |                      Day 1                     |
         --------------------------------------------------
      '''
      output = linebreak
      if ( i < 9 ) :
         output += "\n |                                                                                             Day " + str( i + 1 ) 
         output += "                                                                                                      |\n"

      elif ( i < 99 ) :
         output += "\n |                                                                                             Day " + str( i + 1 ) 
         output += "                                                                                                     |\n"

      else :
         output += "\n |                                                                                             Day " + str( i + 1 ) 
         output += "                                                                                                    |\n"


      output += linebreak
      '''
         --------------------------------------------------
         |  Time  | 00:00 | 01:00 | 02:00 | 03:00 | 04:00 |
         --------------------------------------------------
      '''
      output += "\n |  Time  | "
      for j in range ( numOfHours ) :
     
         if ( j < 10 ) :
            output += "0" + str( j ) + ":00 | "
         else : 
            output += str( j ) + ":00 | "
 
      '''
         --------------------------------------------------
         | EMS  0 |   x   |   x   |   x   |   x   |   x   |
         --------------------------------------------------
         | EMS  1 |   x   |   x   |   x   |   x   |   x   |  
         --------------------------------------------------
         | EMS  2 |   x   |   x   |       |   x   |   x   | 
         --------------------------------------------------
         | EMS  3 |       |   x   |   x   |   x   |   x   | 
         --------------------------------------------------
         | EMS  4 |   x   |   x   |   x   |       |   x   |   
         --------------------------------------------------
      '''
      for k in range ( numOfAmbulances ) :

         output += "\n" + linebreak + "\n"

         if ( k < 9 ) :
            output += " | EMS  " + str( k + 1 ) + " |  "
         else :
      	    output += " | EMS " + str( k + 1 ) + " |  "

         for j in range ( numOfHours ) :
  
            if ( availability_table[i][ j ][ k ] == 0 ) : 
               output += " x "
            else :
               output += "   "

            output += "  |  "
      output += "\n" + linebreak + "\n"

      '''
         --------------------------------------------------
         | Code 0 |       |  Yes  |       |       |  Yes  |
         --------------------------------------------------
      '''
      output += " | Code 0 | "
      global codeZero
      for j in range ( numOfHours) :
         codeZero = True
         for k in range ( numOfAmbulances ) :
         
            if ( availability_table[i][ j ][ k ] == 1 ) : 
               codeZero = False 

         if ( codeZero ) :
            output += " Yes  | "
         else :
            output += "      | "


      output += "\n" + linebreak + "\n" 

      # debug Code
      print ( output )

      # Save the output to file
      output += "\n" 
      text_file = open( output_file , "a" )
      text_file.write( output )
      text_file.close( )



numOfAmbulances = 12
numOfHours = 24
numOfDays = 365

availability_table = [ [ [ 0 for ambulances in range ( numOfAmbulances ) ] for hours in range ( numOfHours  ) ] for days in range ( numOfDays ) ]

# availability_table [day][ hour ][EMS #]
availability_table [1][ 4 ][ 5 ] = 1

# debug Code
# pprint.pprint ( availability_table )
display_availability_table ( availability_table, "Output.txt" )



