# This file is generated by /build/python-numpy-GtMZUd/python-numpy-1.11.0/setup.py
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

atlas_3_10_info={}
blas_opt_info={'define_macros': [('NO_ATLAS_INFO', 1), ('HAVE_CBLAS', None)], 'libraries': ['blas', 'blas'], 'language': 'c', 'library_dirs': ['/usr/lib']}
blas_mkl_info={}
mkl_info={}
atlas_3_10_threads_info={}
lapack_opt_info={'define_macros': [('NO_ATLAS_INFO', 1), ('HAVE_CBLAS', None)], 'libraries': ['lapack', 'lapack', 'blas', 'blas'], 'language': 'c', 'library_dirs': ['/usr/lib']}
atlas_blas_threads_info={}
atlas_3_10_blas_threads_info={}
blas_info={'libraries': ['blas', 'blas'], 'library_dirs': ['/usr/lib'], 'language': 'c', 'define_macros': [('HAVE_CBLAS', None)]}
atlas_3_10_blas_info={}
atlas_info={}
atlas_threads_info={}
openblas_info={}
atlas_blas_info={}
openblas_lapack_info={}
lapack_info={'libraries': ['lapack', 'lapack'], 'library_dirs': ['/usr/lib'], 'language': 'f77'}
lapack_mkl_info={}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    