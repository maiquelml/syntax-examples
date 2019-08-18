## Basic syntax with Ruby ##

####################################################
# Class
class Inicial
  def initialize
    # like constructor
    puts('The class is ready!')
  end

  def soma(a, b)
    # last instruction in method is return
    a + b
  end

  def setVariables(varOne, varTwo)
    @firstVar, @secondVar = varOne, varTwo
  end

  def printVariables
    puts @firstVar + ' ' + @secondVar
  end
end

inicial = Inicial.new
puts inicial.soma(1,2)

inicial.setVariables('Hello', 'World')
inicial.printVariables

####################################################
# For and Range
for i in 2..8
  # print 8
  if i > 7
    puts i
  end
end