package com.iste.iot.ble.auxiliary;

/*
 * Created by Abhishek on 04-01-2016.
 */

import android.annotation.TargetApi;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.le.ScanResult;
import android.os.Build;

public class Beacon {
    private BluetoothDevice bluetoothDevice;
    private int rssi;
    private ScanResult scanResult;
    private byte[] scanRecordBytes;

    public Beacon(BluetoothDevice bluetoothDevice, int rssi, byte[] scanRecordBytes) {
        this.bluetoothDevice = bluetoothDevice;
        this.rssi = rssi;
        this.scanRecordBytes = scanRecordBytes;
    }

    @TargetApi(Build.VERSION_CODES.LOLLIPOP)
    public Beacon(ScanResult scanResult) {
        this.scanResult = scanResult;
        this.bluetoothDevice = scanResult.getDevice();
        this.rssi = scanResult.getRssi();
        this.scanRecordBytes = scanResult.getScanRecord().getBytes();
    }

    public BluetoothDevice getBluetoothDevice() {
        return bluetoothDevice;
    }

    public int getRssi() {
        return rssi;
    }

    public byte[] getScanRecordBytes() {
        return scanRecordBytes;
    }

    public ScanResult getScanResult() {
        return scanResult;
    }
}
