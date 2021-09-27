import time
from valveexe import ValveExe
from valvebsp import Bsp
from valveexe.console import ExecConsole, RconConsole
from totcommon.logger import stdout



def buildcubemaps(bspPath, mapName, gameExe, gameDir, steamExe, steamId):

    valveExe = ValveExe(gameExe, gameDir, steamExe, steamId)
    stdout('Launching game...')
    valveExe.launch(['-windowed', '-novid', '-nosound', 
                     '+mat_hdr_level', '2', '+mat_specular', '0',
                     '+map', mapName, ])

    stdout('Detecting dynamic ranges...')
    
    bsp = Bsp(bspPath)

    ldr = bsp.header.lump_t[8].filelen > 0
    hdr = bsp.header.lump_t[53].filelen > 0
    cnt = bsp.header.lump_t[42].filelen / 16

    cubes_completed = 'sample: {0}/{0}'.format(int(cnt))
    map_loaded = "Redownloading all lightmaps|connected\."
    hdr_changed = "Redownloading all lightmaps|Can't save multiplayer games."
 
    with valveExe as console:
        stdout('Waiting for map load...')                
        valveExe.logger.log_until(map_loaded)

        def run_cubemaps(cfg=None):
            valveExe.logger.log_ingest()
            if cfg == 'hdr':
                stdout('Generating HDR Cubemaps...')
            elif cfg == 'ldr':
                stdout('Generating LDR Cubemaps...')
                console.run('mat_hdr_level', '0')
                hlogs = valveExe.logger.log_until(hdr_changed)

                if "Can't save multiplayer games." in hlogs:
                    console.run('map', mapName)
                    valveExe.logger.log_until(map_loaded)
            else:
                stdout('Generating Cubemaps...')

            console.run('buildcubemaps')
            if isinstance(console, ExecConsole):
                valveExe.logger.log_until(cubes_completed)

        if ldr and hdr:
            run_cubemaps('hdr')
            run_cubemaps('ldr')
        else:
            run_cubemaps()

        if isinstance(console, ExecConsole):
           valveExe.logger.log_until(map_loaded)

        if (valveExe.hijacked):
            console.run("disconnect")
        else:
            console.run("quit")

    del valveExe

    stdout('Generation complete!')