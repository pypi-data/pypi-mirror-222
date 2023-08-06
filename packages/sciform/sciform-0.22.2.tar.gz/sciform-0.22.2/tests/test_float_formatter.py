import unittest

from sciform import Formatter, ExpMode, GroupingSeparator, FillMode


FloatFormatterCases = list[tuple[float, list[tuple[Formatter, str]]]]


class TestFormatting(unittest.TestCase):
    def run_float_formatter_cases(self, cases_list: FloatFormatterCases):
        for num, formats_list in cases_list:
            for formatter, expected_num_str in formats_list:
                snum_str = formatter(num)
                with self.subTest(num=num,
                                  expected_num_str=expected_num_str,
                                  actual_num_str=snum_str):
                    self.assertEqual(snum_str, expected_num_str)

    def test_superscript_exp(self):
        cases_list = [
            (789, [
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           superscript_exp=True), '7.89×10²')
            ])
        ]

        self.run_float_formatter_cases(cases_list)

    def test_fill_and_separators(self):
        cases_list = [
            (123456789.654321, [
                (Formatter(
                    upper_separator=GroupingSeparator.UNDERSCORE,
                    lower_separator=GroupingSeparator.UNDERSCORE,
                    fill_mode=FillMode.ZERO,
                    top_dig_place=14), '000_000_123_456_789.654_321'),
                (Formatter(
                    upper_separator=GroupingSeparator.UNDERSCORE,
                    lower_separator=GroupingSeparator.UNDERSCORE,
                    fill_mode=FillMode.SPACE,
                    top_dig_place=14), '      123_456_789.654_321'),
            ]),
            (4567899.7654321, [
                (Formatter(
                    upper_separator=GroupingSeparator.UNDERSCORE,
                    lower_separator=GroupingSeparator.UNDERSCORE,
                    fill_mode=FillMode.ZERO,
                    top_dig_place=14), '000_000_004_567_899.765_432_1'),
                (Formatter(
                    upper_separator=GroupingSeparator.UNDERSCORE,
                    lower_separator=GroupingSeparator.UNDERSCORE,
                    fill_mode=FillMode.SPACE,
                    top_dig_place=14), '        4_567_899.765_432_1'),
            ])
        ]

        self.run_float_formatter_cases(cases_list)

    def test_latex(self):
        cases_list = [
            (789, [
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           latex=True), r'7.89\times 10^{+2}'),

                # Latex mode takes precedence over superscript_exp
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           latex=True,
                           superscript_exp=True), r'7.89\times 10^{+2}')
            ]),
            (12345, [
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           exp=-1,
                           upper_separator=GroupingSeparator.UNDERSCORE,
                           latex=True), r'123\_450\times 10^{-1}'),
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           exp=3,
                           prefix_exp=True,
                           latex=True), r'12.345\text{k}')
            ])
        ]

        self.run_float_formatter_cases(cases_list)

    def test_nan(self):
        cases_list = [
            (float('nan'), [
                (Formatter(percent=True), '(nan)%'),
                (Formatter(percent=True,
                           latex=True), r'\left(nan\right)\%')
            ])
        ]

        self.run_float_formatter_cases(cases_list)

    def test_parts_per_exp(self):
        cases_list = [
            (123e-3, [
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           exp=-3,
                           parts_per_exp=True,
                           add_ppth_form=True), '123 ppth'),
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           exp=-6,
                           parts_per_exp=True), '123000 ppm'),
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           exp=-2,
                           parts_per_exp=True), '12.3e-02')
            ]),
            (123e-9, [
                (Formatter(exp_mode=ExpMode.ENGINEERING,
                           parts_per_exp=True), '123 ppb'),
                (Formatter(exp_mode=ExpMode.ENGINEERING,
                           parts_per_exp=True,
                           extra_parts_per_forms={-9: None, -12: 'ppb'}),
                 '123e-09')
            ]),
            (123e-12, [
                (Formatter(exp_mode=ExpMode.ENGINEERING,
                           parts_per_exp=True), '123 ppt'),
                (Formatter(exp_mode=ExpMode.ENGINEERING,
                           parts_per_exp=True,
                           extra_parts_per_forms={-9: None, -12: 'ppb'}),
                 '123 ppb')
            ])
        ]

        self.run_float_formatter_cases(cases_list)


if __name__ == "__main__":
    unittest.main()
