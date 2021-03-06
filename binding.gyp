{
    "variables":{
        'default_lib_dir':'/usr/bin/x86_64-linux-gnu-ld',
        'cv_lib_dir': '/home/arjunkava/Work/caffenode-js/node_modules/caffenode-js-build/opencv/build/lib',
        'caffe_lib_dir': '/home/arjunkava/Work/caffenode-js/node_modules/caffenode-js-build/caffe/caffe/build/lib',
        'cv_include':'/home/arjunkava/Work/caffenode-js/node_modules/caffenode-js-build/opencv/build/include',
        'cv_src_include':'/home/arjunkava/Work/caffenode-js/node_modules/caffenode-js-build/caffe/caffe/build/src',
        'caffe_include':'/home/arjunkava/Work/caffenode-js/node_modules/caffenode-js-build/caffe/caffe/include',
        'caffe_proto_include':'/home/arjunkava/Work/caffenode-js/node_modules/caffenode-js-build/caffe/caffe/src/'
    },
    "targets": [
        {
            "target_name": "caffenodejs",
            "defines":[
                "CPU_ONLY=1"
            ],
            "sources": [
                "binding/caffenodejs.cc",
                "binding/caffe/caffenode_blob.h",
                "binding/caffe/caffenode_blob.cc",
                "binding/utils/debug.h",
                "binding/utils/status.h"
            ],
            'include_dirs': [
               '<(caffe_include)',
               '<(caffe_proto_include)',
            ],
            'libraries': [
                '<@(caffe_lib_dir)/libcaffe.a',
                '-lprotobuf',
                '-lboost_system',
                '-lpthread'
            ],
            'library_dirs' : [
                '<(caffe_lib_dir)',
            ],
            "cflags" : [
    			"-std=c++11"
            ],
            "cflags!" : [
                "-fno-exceptions"
            ],
            "cflags_cc!": [
                "-fno-rtti",
                "-fno-exceptions",
                '-Wno-ignored-qualifiers'
            ],
            "configurations": {
                "Debug": {
                    "cflags": ["--coverage"],
                    "ldflags": ["--coverage"]
                },
            }
        }
    ]
}
