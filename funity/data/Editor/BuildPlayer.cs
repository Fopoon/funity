using JetBrains.Annotations;
using UnityEditor;
using UnityEngine;
using static funity.Utils;

namespace funity
{
    public static class BuildPlayer
    {
        [UsedImplicitly]
        public static void Android()
        {
            Build(CreatePlayerBuilder(
                      Application.productName,
                      BuildTarget.Android
                  ));
        }

        [UsedImplicitly]
        public static void Ios()
        {
            Build(CreatePlayerBuilder(
                      Application.productName,
                      BuildTarget.iOS
            ));
        }

        [UsedImplicitly]
        public static void Target()
        {
            Build(CreatePlayerBuilder(
                      Application.productName,
                      EditorUserBuildSettings.activeBuildTarget
                  ));
        }

        private static IPlayerBuilder CreatePlayerBuilder(
            string name,
            BuildTarget target
        )
        {
            return new PlayerBuilder
            {
                Name = name,
                Target = target
            };
        }

        private static void Build(IPlayerBuilder playerBuilder)
        {
            Log($"{nameof(BuildPlayer)}.{playerBuilder.Target}");

            var success = playerBuilder.Build();

            Quit(success);
        }
    }
}