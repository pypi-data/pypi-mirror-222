import unittest

from sciform import Formatter, ExpMode, GroupingSeparator


ValUncFormatterCases = list[tuple[tuple[float, float],
                                  list[tuple[Formatter, str]]]]


class TestFormatting(unittest.TestCase):
    def run_val_unc_formatter_cases(self, cases_list: ValUncFormatterCases):
        for (val, unc), formats_list in cases_list:
            for formatter, expected_val_unc_str in formats_list:
                snum_str = formatter(val, unc)
                with self.subTest(val=val, unc=unc,
                                  expected_num_str=expected_val_unc_str,
                                  actual_num_str=snum_str):
                    self.assertEqual(snum_str, expected_val_unc_str)

    def test_bracket_unc(self):
        cases_list = [
            ((123.456, 0.789), [
                (Formatter(bracket_unc=True), '123.456(789)'),
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           bracket_unc=True), '(1.23456(789))e+02'),
                (Formatter(exp_mode=ExpMode.ENGINEERING,
                           bracket_unc=True), '(123.456(789))e+00'),
                (Formatter(exp_mode=ExpMode.ENGINEERING_SHIFTED,
                           bracket_unc=True), '(0.123456(789))e+03'),
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           exp=+1,
                           bracket_unc=True), '(12.3456(789))e+01'),
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           exp=-1,
                           bracket_unc=True), '(1234.56(7.89))e-01'),
            ])
        ]

        self.run_val_unc_formatter_cases(cases_list)

    def test_percent(self):
        cases_list = [
            ((0.123_456_78, 0.000_002_55), [
                (Formatter(percent=True,
                           lower_separator=GroupingSeparator.UNDERSCORE),
                 '(12.345_678 +/- 0.000_255)%'),
                (Formatter(percent=True,
                           bracket_unc=True,
                           lower_separator=GroupingSeparator.UNDERSCORE),
                 '(12.345_678(255))%')
            ])
        ]

        self.run_val_unc_formatter_cases(cases_list)

    def test_bracket_unc_remove_dec_symb(self):
        cases_list = [
            ((123.456, 0.789), [
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           exp=-1,
                           bracket_unc=True), '(1234.56(7.89))e-01'),
                (Formatter(
                    exp_mode=ExpMode.SCIENTIFIC,
                    exp=-1,
                    bracket_unc_remove_seps=True,
                    bracket_unc=True), '(1234.56(789))e-01'),
            ]),
            ((0.789, 123.456), [
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           exp=-1,
                           bracket_unc=True), '(7.89(1234.56))e-01'),
                # Don't remove "embedded" decimal unless val > unc.
                (Formatter(
                    exp_mode=ExpMode.SCIENTIFIC,
                    exp=-1,
                    bracket_unc_remove_seps=True,
                    bracket_unc=True), '(7.89(1234.56))e-01'),
            ])
        ]

        self.run_val_unc_formatter_cases(cases_list)

    def test_unc_pm_whitespace(self):
        cases_list = [
            ((123.456, 0.789), [
                (Formatter(unc_pm_whitespace=True), '123.456 +/- 0.789'),
                (Formatter(unc_pm_whitespace=False), '123.456+/-0.789')
            ])
        ]

        self.run_val_unc_formatter_cases(cases_list)

    def test_unicode_pm(self):
        cases_list = [
            ((123.456, 0.789), [
                (Formatter(unicode_pm=True), '123.456 ± 0.789')
                ])
        ]

        self.run_val_unc_formatter_cases(cases_list)

    def test_superscript_exp(self):
        cases_list = [
            ((789, 0.01), [
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           superscript_exp=True), '(7.8900 +/- 0.0001)×10²')
            ])
        ]

        self.run_val_unc_formatter_cases(cases_list)

    def test_latex(self):
        cases_list = [
            ((12345, 0.2), [
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           exp=-1,
                           upper_separator=GroupingSeparator.UNDERSCORE,
                           latex=True),
                 r'\left(123\_450 \pm 2\right)\times 10^{-1}'),

                # Latex mode takes precedence over unicode_pm
                (Formatter(exp_mode=ExpMode.SCIENTIFIC,
                           exp=-1,
                           upper_separator=GroupingSeparator.UNDERSCORE,
                           unicode_pm=True,
                           latex=True),
                 r'\left(123\_450 \pm 2\right)\times 10^{-1}')
            ]),
            ((0.123_456_78, 0.000_002_55), [
                (Formatter(lower_separator=GroupingSeparator.UNDERSCORE,
                           percent=True,
                           latex=True),
                 r'\left(12.345\_678 \pm 0.000\_255\right)\%'),
                (Formatter(lower_separator=GroupingSeparator.UNDERSCORE,
                           percent=True,
                           bracket_unc=True,
                           latex=True),
                 r'\left(12.345\_678\left(255\right)\right)\%')
            ])
        ]

        self.run_val_unc_formatter_cases(cases_list)

    def test_pdg(self):
        cases_list = [
            ((10, 0.0353), [
                (Formatter(pdg_sig_figs=True), '10.000 +/- 0.035')
            ]),
            ((10, 0.0354), [
                (Formatter(pdg_sig_figs=True), '10.000 +/- 0.035')
            ]),
            ((10, 0.0355), [
                (Formatter(pdg_sig_figs=True), '10.00 +/- 0.04')
            ]),
            ((10, 0.0949), [
                (Formatter(pdg_sig_figs=True), '10.00 +/- 0.09')
            ]),
            ((10, 0.0950), [
                (Formatter(pdg_sig_figs=True), '10.00 +/- 0.10')
            ]),
            ((10, 0.0951), [
                (Formatter(pdg_sig_figs=True), '10.00 +/- 0.10')
            ])
        ]

        self.run_val_unc_formatter_cases(cases_list)


if __name__ == "__main__":
    unittest.main()
