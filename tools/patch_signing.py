import re
p = 'android/app/build.gradle'
s = open(p).read()
block = """
    signingConfigs {
        debug {
            storeFile file('../../debug.keystore')
            storePassword 'android'
            keyAlias 'androiddebugkey'
            keyPassword 'android'
        }
    }
"""
assert 'debug.keystore' not in s
s2 = re.sub(r'(^android\s*\{)', lambda m: m.group(1) + block, s, count=1, flags=re.M)
assert s2 != s and 'debug.keystore' in s2
open(p, 'w').write(s2)
print('signing config added')
