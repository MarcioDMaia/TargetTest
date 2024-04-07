

class Target:
    
    def __init__(self, command):
        self.command = command


    def self_function(self, complement=None):
        match self.command:

            case 1:
                self.question_one()
                 
            case 2:
                self.question_two(fib=complement)

            case 3:
                self.question_three()

            case 4:
                self.question_four()

            case 5:
                self.question_five(word=complement)

    def question_one(self):
        print(sum([i for i in range(14)]))

    def question_two(self, fib):
        fibonacci = [1, 1]
        while fib >= fibonacci[-1]:
            fibonacci.append(fibonacci[-1]+fibonacci[-2])
        
        if fib in fibonacci:
            print(f"Este número {fib} faz parte da sequência de Fibonacci.")
        else:
            breakpoint()
            print(f"Este número {fib} não faz parte da sequencia de Fibonacci.")

    def question_three(self):
        print("A sequência da letra a, respeita a seguinte ordem de criação: Pn = n + (n+1), onde n = 0,1,2,...,°°. Logo o próximo número da sequência é: 9")
        print("A sequência da letra b, respeita a seguinte ordem de criação: Pn = 2**n, onde n = 1, 2, 3, 4,...,°°. Logo o próximo número da sequência é: 128")
        print("A sequência da letra c, respeita a seguinte ordem de criação: P0 = 0, Pn = n ** 2, onde n = 0, 1, 2, 3, 4, ..., °°. Logo o próximo número da sequência é: 49")
        print("A sequência da letra d, respeita a seguinte ordem de criação: £ = m/2 onde £ != 0 onde m = 1, 3, 5,..., 1777, P1 = 4*m(1), Pn = P1*m(n-1)+m(n), ou seja o próximo número da sequência é: 84 ")
        print("A sequência da letra e, respeita a seguinte ordem de criação da sequÊncia de fibonacci, logo o próximo da sequência é: 13")
        print("A sequÊncia da letra f, tem como orndem de criação números que comecem com a letra d, tornando assim o próximo número da sequência o número 200")
    
    def question_four(self):
        print("Para descobrir quais luzes são comandadas por quais enterruptores, inicialmente acenderia duas luzes, veria quais acenderam, após\nisso, apagaria apenas o enterruptor do meio e acenderia o que ainda não foi mexido, voltaria na sala das lampadas e assim descobrindo quais enterruptores controlam cada lampada")
        print("Ao apagar apenas uma das lampadas, a que apagou revela qual interruptor manda nelas, descobrindo assim, as 3 ao ver qual lampada apagou na segunda visita. Assim deixando claro, que a lampada que permanececu acesa durante a segunda vistoria, é do enterruptor que não foi mexido para a segunda vistoria")
        print("Enquando que o enterruptor que foi apagado para a segunda vistoria, é o mandante da outra luz, sobrando apenas a terceira que foi acendida na segunda vistoria")

    def question_five(self, word):
        print(word[::-1])


    def loop(self):
        list_complement  = [13, 34, 10, 10, "Marcio"]
        for i in range(1, 6):
            self.command = i
            if self.command in [2,5]:
                a = list_complement[self.command-1]
                
                self.self_function(complement=a)
            else:
                self.self_function()


if __name__ == "__main__":
    object_Target = Target(1)
    object_Target.loop()
