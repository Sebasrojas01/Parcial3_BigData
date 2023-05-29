import unittest
from kinesis import get_data
from unittest.mock import patch

# La prueba unitaria
class MyTest(unittest.TestCase):
    
    @patch('__main__.get_data')
    def test_get_data(self, mock_get_data):
        # Definimos el comportamiento simulado del parche
        mock_get_data.return_value = {'date': '2023-05-25 16:19:17',
                                      'close': 4520.810464}

        # Llamamos a la función que estamos probando
        result = get_data()

        # Verificamos si el resultado es el esperado
        self.assertEqual(result, {'date': '2023-05-25 16:19:17',
                                  'close': 4520.810464})

if __name__ == '__main__':
    unittest.main()