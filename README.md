Python interface to the Berkeley Parser
---------------------------------------

This has the advantage over other implementations which essentially automate a call to the jar file: this actually duplicates the `main` method, allowing multiple parse calls and ability to modify options without the overhead of loading the grammar file each time (and without having to use Java!)

**N.B.** several features completely ignored (notably, `-nThreads`, `-nGrammars`, `-kbest` options) and some theoretically implemented but untested (`-chinese`)

See example.py for a short running demo of the interface.

## Installation and Dependencies ##

Although a package script has been setup to install the Python module, one dependency cannot currently be fulfilled by PyPi- the core bridge between Python and Java, JPype. The authors have submitted a support request to have JPype included into PyPi, but until that time, you'll have to download and install this dependency yourself.

Download the JPype package from [JPype 0.5.4.2](http://jpype.sourceforge.net/) and unpackage it in your current working directory. Run the command:

    pip install JPype-0.5.4.2

Which should begin the installation process (we highly recommend that you use virtualenv and virtualenvwrapper to do this). Then simply run:

    python setup.py install

And the BerkeleyInterface package should be installed into your Python path.

*Note*: For Mac users, you may have to modify JPype's settings a bit, according to this [Stackoverflow Question](http://stackoverflow.com/questions/18524501/installing-jpype-in-mountain-lion). Modify the `JPype-0.5.4.2/setup.py` file to include the line following line:

    def setupInclusion(self):
        self.includeDirs = [
            self.javaHome+"/include",
            self.javaHome+"/include/"+self.jdkInclude,
            "src/native/common/include",
            "src/native/python/include",

            #I added this line below. The folder contains a jni.h
            "/System/Library/Frameworks/JavaVM.framework/Versions/A/Headers/"
        ]

Then run the `pip install JPype-0.5.4.2` command and it should work.
