from sys import argv

def writeJoy(f, n):
    f.write('  <node pkg="joy" type="joy_node" name="joy{}">\n'.format(n))
    f.write('    <remap from="joy" to="joy/{}"/>\n'.format(n))
    f.write('    <param name="dev" type="string" value="/dev/input/js{}"/>\n'.format(n))
    f.write('    <param name="deadzone" value="0.0" />\n')
    f.write('    <param name="autorepeat_rate" value="100.0" type="double"/>\n')
    f.write('  </node>\n')

def genLaunch(N, debug):
    filename="multijoy{}.launch".format(N)
    out=open(filename, 'w')
    
    out.write('<launch>\n')
    for n in xrange(N):
        writeJoy(out, n)
    out.write('  <node pkg="multijoy" name="multijoy_node" type="multijoy_node.py" output="screen">\n')
    out.write('    <param name="njoys" type="int" value="{}"/>\n'.format(N))
    if debug:
        out.write('    <param name="debug" type="bool" value="true"/>\n')
    out.write('  </node>\n')
    out.write('</launch>')
    out.close()
    print "MultiJoy launch created: {}".format(filename)

if __name__=='__main__':

    if len(argv)<2:
        print "Useage:"
        print "  $ python generate.py N [debug]"
        print "N is the number of joys"
        print "if debug is written then a debug parameter will appear in launch file"

    N=int(argv[1])
    if len(argv)==3:
        if argv[2]=='debug':
            debug=True
        else:
            debug=False
    else:
        debug=False
    genLaunch(N,debug)
