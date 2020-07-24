using UnityEditor;

namespace funity
{
    public interface IPlayerBuilder
    {
        BuildTarget Target { get; set; }

        bool Build();
    }
}