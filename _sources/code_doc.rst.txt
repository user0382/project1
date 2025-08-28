Code documentaion
------------------

.. note:: 

  To document python code, you can use ``.. py:function::``. Example below:

.. py:function:: get_sum(a : int, b : int)

   Return sum of two integer
   
   :param kind: a, b
   :type kind: int
   :return: sum of two ints
   :rtype: int
   
.. testsetup::

   from test import get_sum

.. doctest::

   >>> get_sum(4, 5)
   9
