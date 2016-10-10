MC504
=====

Repositório criado para o armazenamento de material para a discplina de Sistemas Operacionais.

Para rodar o programa, execute final.py


Projeto 1 – Problema dos Produtores e Consumidores


	  Para este projeto foi escolhido o problema dos Produtores e Consumidores, como apresentado 
	no livro The Little Book on Semaphores. Foi desenvolvido um algoritmo para tratar N threads 
	consumidoras e M threads produtoras, porém devido à limitação de tamanho na parte gráfica é 
	possível alocar em torno de 10 consumidores e produtores apesar de o algoritmo ser funcional 
	para qualquer número de threads.
	
	  Escolhemos trabalhar em python neste projeto pois esta linguagem apresenta facilidades consideráveis 
	para se tratar de representações gráficas e pois ela possui uma biblioteca para threads semelhante à 
	biblioteca usada em sala de aula. Utilizamos as bibliotecas array e threading para o motor do algoritmo 
	de sincronização e a biblioteca Tkinter para a representação gráfica.
	  
	  Após o delegação de tarefas desenvolvemos separadamente a parte de sincronização e a parte gráfica, 
	com o intuito de juntá-las e compor o trabalho final. Como já foi dito a biblioteca Tkinter apresenta 
	facilidades razoáveis porém não pudemos prever que fosse uma biblioteca com um suporte a uma única thread: 
	“main.loop” sendo esta a única thread capaz de realizar mudanças no desenvolvimento gráfico. Perante este 
	impedimento pesquisamos alguma solução e encontramos um módulo, chamado MtTKinter para modificar esta 
	biblioteca possibilitando sua funcionalidade multi-threading. 
	
	  As únicas threads criadas são as de “produtor” e “consumidor”, sendo estas sincronizadas por meio de 
	três semáforos: um mutex para assegurar o acesso exclusivo à área crítica(representada pelo caminho 
	percorrido pelo personagem), um para garantir que o buffer(pilha de pratos) não estoure seu limite máximo 
	de elementos, e outro para impedir que o consumidor tente consumir um prato(elemento do buffer) ainda não produzido.
	Na animação utilizamos um pequeno cenário desenhado por nós para representar o estado geral da aplicação, 
	este cenário consiste de: no lado esquerdo os produtores alinhados, no lado direito os consumidores e entre 
	eles um caminho para a mesa, que representa o buffer, responsável por carregar os elementos(pratos). Quando 
	uma thread atinge a região crítica esta, bloqueando todas as outras, ativa a animação para o personagem 
	equivalente à thread, levando-o à mesa para realizar sua ação pré-definida, retirar ou colocar pratos, ao final 
	desta ação o personagem volta para o seu lugar original na “fila” e espera enquanto outra thread entra na região 
	critica.
