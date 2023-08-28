#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: captain
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class TxRx_FM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "TxRx_FM")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2.4e6
        self.Gain_TxRx_B1 = Gain_TxRx_B1 = 30
        self.Gain_TxRx_A1 = Gain_TxRx_A1 = 30
        self.Gain = Gain = 30
        self.Frec_TxRx_B1 = Frec_TxRx_B1 = 100e6
        self.Frec_TxRx_A1 = Frec_TxRx_A1 = 400e6
        self.Frec_Tomada = Frec_Tomada = 107.15e6

        ##################################################
        # Blocks
        ##################################################
        self._Gain_TxRx_B1_range = Range(0, 80, 1, 30, 200)
        self._Gain_TxRx_B1_win = RangeWidget(self._Gain_TxRx_B1_range, self.set_Gain_TxRx_B1, "Ganancia RF TxRx_B1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Gain_TxRx_B1_win)
        self._Gain_TxRx_A1_range = Range(0, 80, 1, 30, 200)
        self._Gain_TxRx_A1_win = RangeWidget(self._Gain_TxRx_A1_range, self.set_Gain_TxRx_A1, "Ganancia RF TxRx_A1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Gain_TxRx_A1_win)
        self._Gain_range = Range(0, 80, 1, 30, 200)
        self._Gain_win = RangeWidget(self._Gain_range, self.set_Gain, "Ganancia RF Rx_A1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Gain_win)
        self._Frec_TxRx_B1_range = Range(70e6, 500e6, 0.1e6, 100e6, 200)
        self._Frec_TxRx_B1_win = RangeWidget(self._Frec_TxRx_B1_range, self.set_Frec_TxRx_B1, "Frecuencia variable entre 1MHz y 250MHz - TxRx_B1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Frec_TxRx_B1_win)
        self._Frec_TxRx_A1_range = Range(80e6, 480e6, 0.1e6, 400e6, 200)
        self._Frec_TxRx_A1_win = RangeWidget(self._Frec_TxRx_A1_range, self.set_Frec_TxRx_A1, "Frecuencia variable entre 80MHz y 480MHz - TXRX_A1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Frec_TxRx_A1_win)
        self._Frec_Tomada_range = Range(80e6, 480e6, 0.1e6, 107.15e6, 200)
        self._Frec_Tomada_win = RangeWidget(self._Frec_Tomada_range, self.set_Frec_Tomada, "Frecuencia variable entre 80MHz y 480MHz - Rx_A1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Frec_Tomada_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_clock_source('external', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_source_0.set_center_freq(Frec_Tomada, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0.set_gain(Gain, 0)
        self.uhd_usrp_sink_1_0 = uhd.usrp_sink(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
            "",
        )
        self.uhd_usrp_sink_1_0.set_clock_source('internal', 0)
        self.uhd_usrp_sink_1_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_1_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_sink_1_0.set_center_freq(Frec_TxRx_A1, 0)
        self.uhd_usrp_sink_1_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_1_0.set_gain(Gain_TxRx_A1, 0)

        self.uhd_usrp_sink_1_0.set_center_freq(Frec_TxRx_B1, 1)
        self.uhd_usrp_sink_1_0.set_antenna("TX/RX", 1)
        self.uhd_usrp_sink_1_0.set_gain(Gain_TxRx_B1, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            Frec_Tomada, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, firdes.low_pass(1,samp_rate,140e3,10e3), -250e3, samp_rate)
        self.dc_blocker_xx_0 = filter.dc_blocker_cc(32, True)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.uhd_usrp_sink_1_0, 1))
        self.connect((self.dc_blocker_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.uhd_usrp_sink_1_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TxRx_FM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1,self.samp_rate,140e3,10e3))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.Frec_Tomada, self.samp_rate)
        self.uhd_usrp_sink_1_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_Gain_TxRx_B1(self):
        return self.Gain_TxRx_B1

    def set_Gain_TxRx_B1(self, Gain_TxRx_B1):
        self.Gain_TxRx_B1 = Gain_TxRx_B1
        self.uhd_usrp_sink_1_0.set_gain(self.Gain_TxRx_B1, 1)

    def get_Gain_TxRx_A1(self):
        return self.Gain_TxRx_A1

    def set_Gain_TxRx_A1(self, Gain_TxRx_A1):
        self.Gain_TxRx_A1 = Gain_TxRx_A1
        self.uhd_usrp_sink_1_0.set_gain(self.Gain_TxRx_A1, 0)

    def get_Gain(self):
        return self.Gain

    def set_Gain(self, Gain):
        self.Gain = Gain
        self.uhd_usrp_source_0.set_gain(self.Gain, 0)

    def get_Frec_TxRx_B1(self):
        return self.Frec_TxRx_B1

    def set_Frec_TxRx_B1(self, Frec_TxRx_B1):
        self.Frec_TxRx_B1 = Frec_TxRx_B1
        self.uhd_usrp_sink_1_0.set_center_freq(self.Frec_TxRx_B1, 1)

    def get_Frec_TxRx_A1(self):
        return self.Frec_TxRx_A1

    def set_Frec_TxRx_A1(self, Frec_TxRx_A1):
        self.Frec_TxRx_A1 = Frec_TxRx_A1
        self.uhd_usrp_sink_1_0.set_center_freq(self.Frec_TxRx_A1, 0)

    def get_Frec_Tomada(self):
        return self.Frec_Tomada

    def set_Frec_Tomada(self, Frec_Tomada):
        self.Frec_Tomada = Frec_Tomada
        self.qtgui_freq_sink_x_0.set_frequency_range(self.Frec_Tomada, self.samp_rate)
        self.uhd_usrp_source_0.set_center_freq(self.Frec_Tomada, 0)




def main(top_block_cls=TxRx_FM, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
