package com.iste.iot.ble;

import android.app.Activity;
import android.os.Bundle;
import android.os.RemoteException;
import android.util.Log;
import android.widget.TextView;

import org.altbeacon.beacon.Beacon;
import org.altbeacon.beacon.BeaconConsumer;
import org.altbeacon.beacon.BeaconManager;
import org.altbeacon.beacon.BeaconParser;
import org.altbeacon.beacon.MonitorNotifier;
import org.altbeacon.beacon.RangeNotifier;
import org.altbeacon.beacon.Region;

import java.util.Collection;

public class MainActivity extends Activity implements BeaconConsumer {

    protected static final String TAG = "readme";
    private BeaconManager beaconManager;
    private TextView uuid, minor, rssi;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        uuid = (TextView) findViewById(R.id.uuid_display);
        minor = (TextView) findViewById(R.id.minor);
        rssi = (TextView) findViewById(R.id.rssi);

        beaconManager = BeaconManager.getInstanceForApplication(this);

        beaconManager.getBeaconParsers().add(new BeaconParser().
                setBeaconLayout("m:0-3=4c000215,i:4-19,i:20-21,i:22-23,p:24-24"));
        beaconManager.bind(this);

    }

    @Override
    public void onBeaconServiceConnect() {

        try {
            beaconManager.startRangingBeaconsInRegion(new Region("myRangingUniqueId", null, null, null));

        } catch (RemoteException e) {
        }

        beaconManager.setRangeNotifier(new RangeNotifier() {
            @Override
            public void didRangeBeaconsInRegion(Collection<Beacon> beacons, Region region) {
                if (beacons.size() > 0) {

                    // This is where the distance is printed
                    final String rssiString = beacons.iterator().next().getDistance() + "";
                    Log.i(TAG, "The first beacon I see is about " + rssiString + " meters away.");
                    //rssi.setText(rssiString + " meters");

                    //Toast.makeText(MainActivity.this, rssiString, Toast.LENGTH_SHORT).show();

                    // This is where the UUID, major and minor numbers are printed.
                    final String uuidString = beacons.iterator().next().getId1() + "";
                    final String minorString = beacons.iterator().next().getId3() + "";

                    Log.i(TAG, "Reading…" + "\n" + "proximityUuid:" + " " + uuidString + "\n" +
                            "major:" + " " + beacons.iterator().next().getId2() + "\n" +
                            "minor:" + " " + minorString);

                    //uuid.setText(uuidString);
                    //minor.setText(minorString);

                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            updateViews(uuidString, rssiString, minorString);
                        }
                    });
                }
            }
        });


        beaconManager.setMonitorNotifier(new MonitorNotifier() {

            @Override
            public void didEnterRegion(Region region) {
                Log.i(TAG, "I just saw an beacon for the first time!");
            }

            @Override
            public void didExitRegion(Region region) {
                Log.i(TAG, "I no longer see an beacon");
            }

            @Override
            public void didDetermineStateForRegion(int state, Region region) {
                Log.i(TAG, "I have just switched from seeing/not seeing beacons: " + state);
            }
        });

        try {
            beaconManager.startMonitoringBeaconsInRegion(new Region("myMonitoringUniqueId", null, null, null));

        } catch (RemoteException e) {
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        beaconManager.unbind(this);
    }

    private void updateViews(String uuidString, String rssiString, String minorString) {
        rssi.setText(rssiString + " meters");
        uuid.setText(uuidString);
        minor.setText(minorString);

    }
    /*private TextView uuidDisplay;
    private BluetoothManager bluetoothManager;
    private BluetoothAdapter mBluetoothAdapter;
    private BluetoothLeScanner mBluetoothLeScanner;
    private ScanCallback mScanCallback;
    private BluetoothAdapter.LeScanCallback mLeScanCallback;
    private BluetoothGattCallback mGattCallback;
    private final int REQUEST_ENABLE_BT = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        uuidDisplay = (TextView) findViewById(R.id.uuid_display);

        bluetoothManager = (BluetoothManager) getSystemService(Context.BLUETOOTH_SERVICE);

        if(Build.VERSION.SDK_INT >= 21)
        mScanCallback = new ScanCallback() {
            @Override
            public void onScanResult(int callbackType, ScanResult result) {
                super.onScanResult(callbackType, result);
                beaconFound(new Beacon(result));
            }

            @Override
            public void onScanFailed(int errorCode) {
                super.onScanFailed(errorCode);
                Toast.makeText(MainActivity.this, "LE Scan failed", Toast.LENGTH_SHORT).show();
            }
        };
        mLeScanCallback = new BluetoothAdapter.LeScanCallback() {
            @Override
            public void onLeScan(BluetoothDevice device, int rssi, byte[] scanRecord) {
                beaconFound(new Beacon(device, rssi, scanRecord));
            }
        };

        mGattCallback = new BluetoothGattCallback() {

            @Override
            public void onConnectionStateChange(BluetoothGatt gatt, int status, int newState) {
                //Toast.makeText(MainActivity.this, "Connected to beacon", Toast.LENGTH_SHORT).show();
                Log.i("BLE Conn state changed", ""+newState);
                gatt.discoverServices();
            }

            @Override
            public void onServicesDiscovered(BluetoothGatt gatt, int status) {
                List<BluetoothGattService> services = gatt.getServices();
                Log.i("LE Services disovered: ", services.toString());
                uuidDisplay.setText(services.get(0).getUuid().toString());
            }
        };

        if(isBluetoothEnabled())
            startBluetoothScanning();
    }

    private boolean isBluetoothEnabled() {
        mBluetoothAdapter = bluetoothManager.getAdapter();
        if (mBluetoothAdapter == null || !mBluetoothAdapter.isEnabled()) {
            Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
            startActivityForResult(enableBtIntent, REQUEST_ENABLE_BT);
            return false;
        }
        return true;
    }

    private void startBluetoothScanning() {
        if(Build.VERSION.SDK_INT >= 21) {
            mBluetoothLeScanner = mBluetoothAdapter.getBluetoothLeScanner();
            mBluetoothLeScanner.startScan(mScanCallback);
        }
        else {
            mBluetoothAdapter.startLeScan(mLeScanCallback);
        }
    }

    private void beaconFound(Beacon beacon) {
        Toast.makeText(this, "Beacon found!", Toast.LENGTH_SHORT).show();
        if(Build.VERSION.SDK_INT >= 21)
            mBluetoothLeScanner.stopScan(mScanCallback);
        else
            mBluetoothAdapter.stopLeScan(mLeScanCallback);

        BluetoothDevice mDevice = beacon.getBluetoothDevice();
        //mDevice.
        Log.i("BLE Device: ", mDevice.toString());
        ParcelUuid[] uuids = mDevice.getUuids();
        //uuidDisplay.setText(uuids[0].getUuid().toString());
        BluetoothGatt mBluetoothGatt = mDevice.connectGatt(this, true, mGattCallback);
        mBluetoothGatt.discoverServices();
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if(requestCode == REQUEST_ENABLE_BT)
            if(isBluetoothEnabled())
                startBluetoothScanning();
    }

    @Override
    protected void onPause() {
        super.onPause();

    }*/
}