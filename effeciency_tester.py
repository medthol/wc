import subprocess

cmd = "time" "python wc.py" + ' '+ '/'"testinputs" '/' "filename"

tf = subprocess.Popen (cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
output = tf.communicate()
print (output)

