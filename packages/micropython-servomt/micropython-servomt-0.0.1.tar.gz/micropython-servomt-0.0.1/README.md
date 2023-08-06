# comu

init

    from se.serve import Serve
    
    s = Serve(27)
    s.angulo(180)

loop

    while True:
        s.angulo(s.reangulo()+1)

end
    
    s.exit()