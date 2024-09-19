#!/usr/bin/env python

# Copyright 2018-2020 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import nbconvert

with open("assignment7.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)


with open("assignment7.py", "w") as f:
    f.write(python_file)


from assignment7 import *

class TestSolution(unittest.TestCase):

    def test_fit(self):

        kc = KozenyCarmen('poro_perm.csv')

        kc.fit()

        np.testing.assert_allclose(kc.fit(), np.array([  1.05933127e+01,   2.35173520e+04]), atol=0.001)

    def test_fit_through_zero(self):

        kc = KozenyCarmen('poro_perm.csv')

        kc.fit_through_zero()

        np.testing.assert_allclose(kc.fit_through_zero(),26133.929742741482, atol=0.001)


if __name__ == '__main__':
    unittest.main()
