using UnityEngine;

public class MyMonoBehaviour : MonoBehaviour
{
    #region Fields

    [SerializeField] private string _greeting = "Hello World";

    #endregion

    #region Methods

    private void Start()
    {
        Debug.Log(_greeting);
    }

    #endregion
}